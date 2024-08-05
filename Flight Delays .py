# ## Flight Delays 
# Power BI Track Lab06
# AbdEl-Rhman Ashraf 1/8/2024

get_ipython().system('pip install kaggle')
get_ipython().system('pip install pandas')
get_ipython().system('pip install delta-spark')


import os
os.chdir('/lakehouse/default/Files/RawData')
os.environ['KAGGLE_USERNAME'] = 'My_Username'
os.environ['KAGGLE_KEY'] = 'My_key'
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.dataset_download_files('usdot/flight-delays')


from zipfile import ZipFile

# Open the zip file
with ZipFile('/lakehouse/default/Files/RawData/flight-delays.zip', 'r') as zip_ref:
    # Get a list of CSV files in the zip archive
    csv_files = [f for f in zip_ref.namelist() if f.endswith('.csv')]

    # Read each CSV file into a separate DataFrame
    dataframes = {}
    for file in csv_files:
        with zip_ref.open(file) as csv_file:
            dataframes[file] = pd.read_csv(csv_file)



for filename, df in dataframes.items():
    # Process each DataFrame (e.g., print the first few rows)
    print(f"DataFrame from {filename}:")
    print(df.head())
    print("\n")



import os
# Specify the subfolder name
subfolder_name = '/lakehouse/default/Files/RawData'
# Iterate through each DataFrame and save it in the subfolder
for filename, df in dataframes.items():
    output_file = os.path.join(subfolder_name, f"{filename.replace('.csv', '')}.csv")
    df.to_csv(output_file, index=False)
    print(f"Saved {filename} as {output_file}")

print("All DataFrames saved in the subfolder successfully!")


# Specify the path to your Delta Lake table
delta_table_path = "/lakehouse/default/Tables/flight_delays"

# Iterate through each DataFrame and save it as a Delta Lake table
for filename, df in dataframes.items():
    df.write.format("delta").mode("overwrite").save(f"{delta_table_path}/{filename.replace('.csv', '')}")

print("All DataFrames saved as Delta Lake tables successfully!")




