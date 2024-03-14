import json
import pandas as pd
from geopy import Nominatim
from azure.storage.blob import BlobServiceClient

NO_IMAGE = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/No-image-available.png/480px-No-image-available.png'


def get_wikipedia_page(url):
    import requests

    print("Getting wikipedia page...", url)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # check if the request is successful

        return response.text
    except requests.RequestException as e:
        print(f"An error occured: {e}")


def get_wikipedia_data(html):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')
    # Find the table on the Wikipedia page
    table = soup.find_all("table", {"class": "wikitable sortable sticky-header"})[0]
    # table = soup.find('table', {'class': "wikitable sortable sticky-header"})
    table_rows = table.find_all('tr')
    return table_rows


def extract_wikipedia_data(**kwargs):
    url = kwargs['url']
    html = get_wikipedia_page(url)
    rows = get_wikipedia_data(html)
    data = []
    for i in range(len(rows)):
        tds = list(rows[i].find_all('td'))
        if len(tds):  # Ensuring there are enough elements in 'tds' to avoid 'IndexError'
            values = {
                'rank': i,  # Assuming 'i' starts from 0 for the first row
                'stadium': clean_text(tds[0].text),
                'capacity': clean_text(tds[1].text).replace(',', '').replace('.', ''),
                'region': clean_text(tds[2].text),
                'country': clean_text(tds[3].text).strip(),  # Adjusted for simpler extraction
                'city': clean_text(tds[4].text).strip(),
                'images': "https://" + tds[5].find('img')['src'] if tds[5].find('img') else "NO_IMAGE",
                'home_team': clean_text(tds[6].text)
                # 'home_team': ', '.join([a.text for a in tds[6].find_all('a')])
            }
            data.append(values)
    json_rows = json.dumps(data)
    kwargs['ti'].xcom_push(key='rows', value=json_rows)
    return "OK"


def clean_text(text):
    text = str(text).strip()
    text = text.replace('&nbsp', '')
    if text.find(' ♦'):
        text = text.split(' ♦')[0]
    if text.find('[') != -1:
        text = text.split('[')[0]
    if text.find(' (formerly)') != -1:
        text = text.split(' (formerly)')[0]
    return text.replace('\n', '')


def get_lat_long(country, city):
    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(f'{city}, {country}')

    if location:
        return location.latitude, location.longitude

    return None


def transform_wikipedia_data(**kwargs):
    data = kwargs['ti'].xcom_pull(key='rows', task_ids='extract_data_from_wikipedia')

    data = json.loads(data)

    stadiums_df = pd.DataFrame(data)
    # stadiums_df['location'] = stadiums_df.apply(lambda x: get_lat_long(x['country'], x['city']), axis=1)
    stadiums_df['images'] = stadiums_df['images'].apply(lambda x: x if x not in ['NO_IMAGE', '', None] else NO_IMAGE)
    stadiums_df['capacity'] = stadiums_df['capacity'].astype(int)
    # #
    # # handle the duplicates
    # duplicates = stadiums_df[stadiums_df.duplicated(['location'])]
    # duplicates['location'] = duplicates.apply(lambda x: get_lat_long(x['country'], x['city']), axis=1)
    # stadiums_df.update(duplicates)

    # push to xcom
    kwargs['ti'].xcom_push(key='rows', value=stadiums_df.to_json())

    return "OK"


def write_wikipedia_data(**kwargs):
    from datetime import datetime
    data = kwargs['ti'].xcom_pull(key='rows', task_ids='transform_wikipedia_data')

    data = json.loads(data)
    data = pd.DataFrame(data)

    file_name = ('stadium_cleaned_' + str(datetime.now().date())
                 + "_" + str(datetime.now().time()).replace(":", "_") + '.csv')

    # data.to_csv('data/' + file_name, index=False)
    # Replace with your actual storage account details
    connection_string = "DefaultEndpointsProtocol=https;AccountName=srikardevsa;AccountKey=3AIEiAm6e97ryHuOOvbOThC0WUo1LZzJwyenjbRQHdr8hdy8e82ZPGjNVn5FYkeDy6hr9bWlPTKz+AStaXfjlw==;EndpointSuffix=core.windows.net"

    # Container and blob names
    container_name = "dateng"
    blob_name = f"data/{file_name}"

    # Create Blob service client
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get container client
    container_client = blob_service_client.get_container_client(container_name)

    # Convert dataframe to bytes (in memory)
    csv_content = data.to_csv(index=False, encoding="utf-8").encode("utf-8")

    # Upload the data to blob storage
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(csv_content, blob_type="BlockBlob")

