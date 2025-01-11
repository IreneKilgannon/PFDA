import pandas as pd
import glob as glob

def merge_files(file_path, names, usecols, file_name):
    ''' A function to read multiple files matching a glob expression into a single Pandas DataFrame. 
    It processes the data by performing several transformations and outputs the result as a CSV file.

    Arguments:
        file_path: A file path with glob expressions to specify the files to read.

        names: A list of column names for the DataFrame. 

        usecols: The columns to include in the DataFrame.

        file_name: The name of the output CSV file.
    
    Returns: 
        A CSV file of the merged and processed data, stored in the data directory
    '''

    # Use glob to find csv files in a specified path.
    csv_files = glob.glob(file_path)
    
    # Instantiate an empty dataframe
    merge_df = pd.DataFrame()

    # Loop through each CSV file and append contents to merge_df
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

        # Replace missing values by interpolation
        merge_df.interpolate(method= 'linear', inplace= True)

        # Remove duplicate rows.
        merge_df = merge_df[~merge_df.index.duplicated(keep= 'first')]

        # Resample the data to hourly
        merge_df = merge_df.resample('h').mean()

    # Write to csv file to the data directory
    return merge_df.to_csv(f'data/{file_name}.csv')


def resample_df(df, term):
    '''Resample a DataFrame to calculate the mean values by either weekly, monthly or yearly time intervals.
    
    Arguments:
        df: A DataFrame to be resampled.
        term: The resampling frequency, specified as weekly, monthly or yearly.
    
    Returns: 
        A resampled DataFrame based on the specified term.'''

    if term == 'ME':
        df_monthly = df.resample(term).mean()
        return df_monthly
    
    elif term == 'W':
        df_weekly = df.resample(term).mean()
        return df_weekly
    
    else:
        df_yearly = df.resample(term).mean()
        return df_yearly
    

