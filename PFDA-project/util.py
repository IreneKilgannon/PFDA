#def skip_rows(csv_file):
#    '''Read in a csv file and find row number where the data starts.
#    
#    Parameters:
#        csv_file: csv_file to examine
#        
#    Returns:
#        data_start_idx (int): The number of rows to skip'''
#    
#    # Read the file, skipping metadata rows
#    with open(csv_file, 'r') as file:
#        lines = file.readlines()
#    
#    # Identify the start of the data (row where actual CSV content begins)
#    for i, line in enumerate(lines):
#        if line.lower().startswith('date,'):
#            data_start_idx = i
#    
#    return data_start_idx
#
#
#def extract_location(file_name):
#    '''A function to extract the location from the file name'''
#
#    pattern = r'hly\d{3,4}([A-Z][a-z]+[A-Z]?[a-z]+).csv'
#
#    match = re.findall(pattern, file_name)
#
#    if match:
#        return match[0].lower()
#    else:
#        raise ValueError('File name does not match the expected pattern')
#    
#
#def select_years(df):
#    df = df['2014': '2024']
#    return df
#
#def find_files():
#
#    csv_files = glob.glob('data/electricity/*.csv')
#
#    return csv_files

import pandas as pd
import glob as glob

def merge_files(file_path, names, usecols, filename):

    csv_files = glob.glob(file_path)
    
    merge_df = pd.DataFrame()

# Loop through each CSV file found by glob and append contents to merge_df
    for csv_file in csv_files:
        df = pd.read_csv(csv_file, 
                     header = None, 
                     names = names, 
                     index_col= 'date',
                     parse_dates= ['date'],
                     usecols= usecols)
    
    # Concatenate df to electricity_df
        merge_df = pd.concat([merge_df, df])

    # Sort electricity_df by index
        merge_df.sort_index(inplace= True)

        merge_df.interpolate(method= 'linear', inplace= True)

        merge_df = merge_df[~merge_df.index.duplicated(keep= 'first')]

        merge_df = merge_df.resample('h').mean()

    # Write to csv file
    return merge_df.to_csv(f'data/hourly_{filename}.csv')

merge_files('data/electricity_actual/*.csv', ['date', 'actual', 'location', 'Actual (MW)'], ['date', 'Actual (MW)'], 'actual')

merge_files('data/electricity_demand/*.csv', ['date', 'actual', 'location', 'Demand (MW)'], ['date', 'Demand (MW)'], 'demand')

def resample(df, term):

    if term == 'ME':
        df_monthly = df.resample(term).mean()
        return df_monthly
    else:
        df_yearly = df.resample(term).mean()
        return df_yearly

































