# 2015 Flight Delays Analysis Project

## Project Overview
This project aims to analyze flight delays data to extract meaningful insights and provide visualizations using Power BI. The dataset is sourced from Kaggle and is regularly updated to ensure the latest data is analyzed.

## About Dataset
The dataset can be found on [Kaggle](https://www.kaggle.com/datasets/usdot/flight-delays).

### Context
The U.S. Department of Transportation's (DOT) Bureau of Transportation Statistics tracks the on-time performance of domestic flights operated by large air carriers. Summary information on the number of on-time, delayed, canceled, and diverted flights is published in DOT's monthly Air Travel Consumer Report and in this dataset of 2015 flight delays and cancellations.

## Acknowledgements
The flight delay and cancellation data was collected and published by the DOT's Bureau of Transportation Statistics.

## Key Features
- **Data Extraction**: Utilizing Kaggle API to fetch the latest flight delays data.
- **Data Processing**: Using PySpark in Microsoft Fabric notebooks for data extraction.
- **Data Storage**: Storing the CSV files and saving them in Microsoft Fabric Lakehouse as tables.
- **Data Visualization**: Connecting Microsoft Fabric Lakehouse to Power BI for creating dynamic and interactive dashboards.

## Project Workflow

## Setting Up Kaggle API
Used my Kaggle API credentials. These will be used to authenticate and download the dataset.

## Extracting Data Using PySpark
A PySpark script is used to download and process the data from Kaggle. The following code snippet shows the process:

## Scheduling the Notebook
The Microsoft Fabric notebook is set up to run on a schedule based on business needs to ensure that the data is regularly updated.

## Storing Data in Microsoft Fabric Lakehouse
The processed CSV files are stored in the Microsoft Fabric Lakehouse, making them available as tables for further analysis.

## Connecting to Power BI
Using Power BI Desktop, I connect to the Microsoft Fabric Lakehouse SQL endpoint. This connection allows me to create dynamic reports and dashboards that reflect the latest data from Kaggle.

## Building Dashboards in Power BI
I have created the following dashboards to analyze the flight delays:

### **Summary Dashboard**: Provides an overview of total flights, average delays, and monthly trends.

![Summary Report](https://github.com/user-attachments/assets/3b0e311b-ba10-4d75-b3c4-a8d2fd8ccaaf)

Overall, this dashboard provides a comprehensive overview of flight delays and cancellations in the United States in 2015.

**Key Insights**:

- **Total Flights in 2015**: 5.33 million

- **Delayed Flights**: 1.96 million (36.83% of total flights)

- **Average Delay Time**: 24.54 minutes

- **Total Cancellations**: 87,430

**Airline Performance**:

 - Southwest Airlines Co:
    
  - Highest number of total flights (1.16 million)
  - Highest number of delayed flights (0.53 million)

**Top Airport by Total Flights**:

  - Hartsfield-Jackson Atlanta International Airport is # 1 Airport

**Total Flights by Month**:

  - Highest number of flights: July and August
  - Lowest number of flights: January and February


### **Delay by Airline Company Dashboard**: Analyzes delays by different airline companies.

![Airline Report](https://github.com/user-attachments/assets/b4ffb45e-c437-4822-99be-a03b1aba3314)

This dashboard digs deeper, providing a comprehensive overview of airline performance based on flight delays, cancellations, and on-time departures. The data focuses on key metrics such as total flights, delayed flights, cancellation rates, and average delay times.

**Key Insights**:

**Airline Comparison**:

  - JetBlue Airways has the highest number of delayed flights from BOS.
  - Southwest Airlines Co. has the highest number of on-time flights, but yet, it has the highest number of total cancellations.

**Flight Status Distribution**:
  - 63.17% of flights were on time.
  - 36.83% of flights were delayed.


### **Delay by Airport Dashboard**: Analyzes delays by origin and destination airports.

![Airport Report](https://github.com/user-attachments/assets/7de4a88a-4245-4dd4-ad5d-ee1e70a65ec5)

This dashboard provides a detailed analysis of flight delays across various airports. It focuses on key metrics such as average delay time, reliability, and percentage of delayed flights.

**Key Insights**:

**Average Delay Time**:
  - Wilmington Airport has the highest average delay time at 62 minutes.
  - Valdez Airport has the lowest average delay time at 32 minutes.

**Airport Reliability**:
  - Guam International Airport has the lowest reliability with 67.66% of flights delayed.
  - Valdez Airport has the highest reliability with 95.15% of flights on time.


**Detailed Delay Time Dashboard**: Provides a detailed analysis of delay times.

![Seasons Report](https://github.com/user-attachments/assets/dcdb0700-8c92-4648-a4b1-560f1857de5b)

![Delay by Hour](https://github.com/user-attachments/assets/f9eaa776-0cef-4685-af99-0e4ea6d9d18f)

This dashboard focuses on analyzing flight delays and cancellations based on seasons. It provides insights into seasonal trends and variations in flight performance.

**Key Insights**:

**Seasonal Flight Performance**:
  - Summer has the highest number of total flights (1.54 million) and delayed flights.
  - Fall has the lowest number of total flights (1.38 million) and delayed flights.

**Average Delay Time by Season**:
  - Summer has the highest average delay time at 27.81 minutes.
  - Autumn has the lowest average delay time at 17.17 minutes.

**Delayed Flights by Month**:
  - June has the highest number of delayed flights.
  - September has the lowest number of delayed flights.

**Delayed Flights by hour**:
  - The number of delayed flights by scheduled arrival time increases significantly from early morning to midnight, peaking around 7:00 PM and 9:00 PM.
  - There's a noticeable drop in delayed flights during the late evening and early morning hours.
  - A similar pattern is observed for departure times, with a peak in delayed flights around 6:00 AM.

## Potential Areas for Further Analysis:

- Correlation between airline size and on-time performance/cancellation rates.
- Impact of weather conditions on delays and cancellations.
- Analysis of specific airports or routes with consistently high delay rates.
- Investigation of the root causes of delays, especially during peak times.
- Comparison of delay patterns between weekdays and weekends.

## Project Highlights

- **Automated Data Pipeline**: The integration of Kaggle API, PySpark, Microsoft Fabric, and Power BI ensures an automated pipeline for data extraction, transformation, storage, and visualization.

- **Up-to-Date Insights**: The scheduling of the notebook ensures that the insights in Power BI are always based on the most recent data available from Kaggle.
- **Comprehensive Analysis**: The dashboards provide a detailed analysis of flight delays, helping stakeholders make informed decisions.
