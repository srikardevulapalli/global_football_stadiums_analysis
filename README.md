# Global Football Stadiums Analysis
This repository is dedicated to the Global Football Stadiums Analysis project, a sophisticated data engineering initiative designed to automate the collection, cleansing, and storage of global football stadium data. Utilizing Python for data extraction, Apache Airflow for orchestration, and Spark Pool for advanced visualizations, this project streamlines the process from raw data to actionable insights, culminating in a comprehensive dataset stored in Azure Data Lake ready for analysis with Azure Synapse.

## Table of Contents
- Project Overview
- System Requirements
- Quick Start Guide
- Docker Deployment
- Pipeline Execution
- Architecture and Workflow
- Results & Insights
- Acknowledgements

## Project Overview
The project's goal is to provide an exhaustive analysis platform for football stadium data worldwide, focusing on stadium capacities, locations, and associated football clubs. It involves extracting data from multiple online sources, processing the data for quality and consistency, and leveraging Spark Pool for visual analytics.

## System Requirements
Before initiating the project, ensure the following prerequisites are met:
- Python 3.9 or newer
- Docker
- PostgreSQL
- Apache Airflow 2.6 or above
- Azure Data Lake storage account

## Quick Start Guide
To get started with the Global Football Stadiums Analysis project:

1. Clone the repository:
```bash
git clone https://github.com/srikardevulapalli/global_football_stadiums_analysis.git
```

2. Install the necessary Python packages:

 ```bash
pip install -r requirements.txt
```
## Docker Deployment
This project is optimized for Docker, providing a straightforward setup process:

Initialize the Docker services- 

```bash
docker-compose up -d
```

Access the Airflow interface and trigger the data processing DAG.

![alt text](https://github.com/srikardevulapalli/global_football_stadiums_analysis/blob/main/data/airflow_ui.png?raw=true)

There are 3 steps in the Apache Airflow workflow execution as shown here:

![Screenshot 2024-03-14 at 9 15 10 AM](https://github.com/srikardevulapalli/global_football_stadiums_analysis/assets/111369239/6cf20f02-b8dc-4566-945b-e27f12d67f22)

***extract_data_from_wikipedia***

This task is responsible for the initial step in the data pipeline. It involves reaching out to Wikipedia and using a web scraping tool, such as Beautiful Soup, to extract raw data about football stadiums. The duration of this step indicates it's a relatively quick process, suggesting an efficient extraction mechanism and likely a direct pull of structured data, such as tables from specific Wikipedia pages.

***transform_wikipedia_data***

Following the extraction, the data undergoes a transformation process. This step typically includes cleaning the data (e.g., removing duplicates, handling missing values), normalizing formats (e.g., standardizing integer formats, string casing), and structuring the data into a schema that fits the needs of the analysis or database design. Transformation is crucial to ensure data quality and to prepare the data for effective storage and analysis.

***write_wikipedia_data***

The final step writes the transformed data to a persistent storage solution. Given that the pipeline includes storing data in Azure Data Lake as per the architecture overview, this task likely involves writing data files to the lake using the Azure Blob File System (ABFS) protocol. This ensures the data is saved in a secure, scalable environment and is accessible for further processing, such as analytics in Azure Synapse or other data applications.
 
## Pipeline Execution

The Global Football Stadiums Analysis project utilizes a robust data pipeline that encompasses several stages from data extraction to analytics. Here is a detailed walkthrough of the pipeline as depicted in `DataflowDiagram.png` within the repository:

1. **Data Extraction:**
   - The pipeline begins by sourcing football stadium data from the web, using Beautiful Soup to scrape the necessary information from Wikipedia pages. This step ensures that we have the latest data on stadium capacities, locations, and home teams.

2. **Data Processing with Airflow:**
   - The extracted data is passed to a PostgreSQL database housed within a Docker container. Apache Airflow manages the data workflow, ensuring that the processes are executed in the correct sequence and monitoring their health.
   - The Airflow webserver and scheduler oversee the tasks, allowing for both manual and scheduled runs. The robust orchestration ensures that data moves seamlessly from one stage to the next without bottlenecks.

3. **Data Storage in Azure Data Lake:**
   - Once processed, the data is loaded into Azure Data Lake Storage Gen2, which offers a highly scalable and secure storage solution. Here, the data can be managed using hierarchical namespace features and is ready for analytical processing.

4. **Data Analytics with Azure Synapse:**
   - The project leverages Azure Data Factory (ADF) to further orchestrate the movement of data from the lake to Azure Synapse Analytics. Synapse provides a powerful and dynamic environment to run complex queries and analytics on the stored data.
   - Through Synapse, we can perform deep analyses, create comprehensive reports, and generate insights that are translated into actionable results.

5. **Visualization and Results:**
   - The results from Synapse analytics can then be visualized to provide a clear and concise representation of the data. While this pipeline does not directly incorporate Tableau, the results can be used in any visualization tool that supports integration with Azure services, including Power BI, to create interactive dashboards and reports.

## Architecture and Workflow
The data pipeline's structure is crafted to ensure efficient handling of the data engineering lifecycle. For an illustrative summary of the system's architecture, please view this figure:
![alt text](https://github.com/srikardevulapalli/global_football_stadiums_analysis/blob/main/Webserver.png?raw=True)

## Results and Insights
### Results
In the dataviz.ipynb notebook, we've generated a series of data visualizations using Plotly and Seaborn, which are key in extracting meaningful insights from the Global Football Stadiums Analysis.

Scatter Plot of Stadium Capacity by Region:

This visualization illustrates the total stadium capacities by region, with the size of each marker proportional to the capacity. It suggests that certain regions may have larger or more numerous stadiums, which could correlate with regional popularity in football and investment in sports infrastructure.
Histogram and KDE (Kernel Density Estimate) of Stadium Capacities:

We analyzed the distribution of stadium capacities on a country basis. The histogram, overlaid with a KDE plot, indicates the density and variance of stadium sizes. A peak in the density plot may reveal the most common stadium sizes or capacity ranges.
Horizontal Bar Chart of Home Teams by Country:

The bar chart, sorted by the number of home teams per country, provides an insight into which countries have the most significant number of football teams. This can be a proxy to the popularity and development level of football as a sport within those countries.
Color Scales and Plot Enhancements:

We've applied a color scale to represent different values dynamically, enhancing the readability and aesthetic appeal of our visualizations. This approach helps to quickly identify and differentiate between high and low values across the visualized data.
Cumulative Distribution Function (CDF):

While specific details were not extracted, it's evident that a CDF was also part of the analysis, which is useful to understand the distribution of data values cumulatively and can highlight the proportion of stadiums exceeding certain capacity thresholds.
The visualizations generated in this notebook offer a comprehensive view of the world's football stadium capacities and their distribution across different regions and countries. The analytical insights from this project can aid stakeholders in making informed decisions about sports infrastructure investments and understanding global football popularity trends.

### Insights
**Proportion of Stadiums by Country Pie Chart**

The United States holds the largest proportion of stadiums, indicating a substantial investment in sports infrastructure.
Countries like China and Brazil also have significant shares, reflecting their large populations and cultural emphasis on sports.

**Top 10 Largest Stadiums Bar Chart**

The "Spotify Camp Nou" and "Estadio Azteca" are among the largest stadiums, suggesting these locations are prime venues for major events and have high audience capacities.
There's a diverse representation of countries in the top 10, showing that large-scale stadiums are a global phenomenon.
Stadium Capacity by Region Bubble Chart:

Europe and North America boast substantial total stadium capacities, possibly due to their long-standing football traditions and hosting of numerous international events.
East Asia and South America follow closely, which might be connected to their growing economies and increased focus on global sports presence.

**Stadium Capacity Density Histogram and KDE**

The distribution of stadium capacities skews heavily towards the lower end, with a peak just above zero, indicating that smaller stadiums are far more common than larger ones.
The KDE curve suggests there are outliers with significantly larger capacities, which may be the iconic stadiums known for hosting prestigious events.

**Cumulative Distribution Function (CDF) of Stadium Capacity**

The steep curve at the lower capacity values in the CDF indicates that a large percentage of stadiums have relatively low capacities.
The flattening of the curve as it approaches higher capacities suggests fewer stadiums exist within these higher capacity ranges.

**Number of Home Teams by Country Bar Chart**

The United States leads with the highest number of home teams, which can correlate to a strong domestic league system and a high level of participation in football.
Other countries like Argentina and Malaysia also feature prominently, highlighting their potential as enthusiastic football nations.
