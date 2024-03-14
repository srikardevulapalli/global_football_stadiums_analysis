# Global Football Stadiums Analysis
This repository is dedicated to the Global Football Stadiums Analysis project, a sophisticated data engineering initiative designed to automate the collection, cleansing, and storage of global football stadium data. Utilizing Python for data extraction, Apache Airflow for orchestration, and Spark Pool for advanced visualizations, this project streamlines the process from raw data to actionable insights, culminating in a comprehensive dataset stored in Azure Data Lake ready for analysis with Azure Synapse.

## Table of Contents
- Project Overview
- System Requirements
- Quick Start Guide
- Docker Deployment
- Pipeline Execution
- Architecture and Workflow
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

git clone https://github.com/srikardevulapalli/global_football_stadiums_analysis.git

2. Install the necessary Python packages:

pip install -r requirements.txt
 
## Docker Deployment
This project is optimized for Docker, providing a straightforward setup process:

Initialize the Docker services- 

docker-compose up -d

Access the Airflow interface and trigger the data processing DAG.

![alt text](https://github.com/srikardevulapalli/global_football_stadiums_analysis/blob/main/data/airflow_ui.png?raw=true)


## Pipeline Execution
The data pipeline executes the following tasks:

- Data is sourced using Python scripts that scrape selected web resources.
- The raw data undergoes a cleaning phase to rectify inconsistencies and ensure uniformity.
- Data transformation is performed to shape the data into a format suitable for analysis.
- The processed data is then dispatched to Azure Data Lake, utilizing secure protocols for optimal storage and retrieval efficiency.

## Architecture and Workflow
The data pipeline's structure is crafted to ensure efficient handling of the data engineering lifecycle. For an illustrative summary of the system's architecture, please view this figure:
![alt text](https://github.com/srikardevulapalli/global_football_stadiums_analysis/blob/main/Webserver.png?raw=True)
