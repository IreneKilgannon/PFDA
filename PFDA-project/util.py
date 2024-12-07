def skip_rows(csv_file):
    # Read the file, skipping metadata rows
    with open(csv_file, 'r') as file:
        lines = file.readlines()
    
    # Identify the start of the data (row where actual CSV content begins)
    for i, line in enumerate(lines):
        if line.lower().startswith('date,'):
            data_start_idx = i
    
    return data_start_idx

def extract_location(file_name):
    '''A function to extract the location from the file name'''

    pattern = r'hly\d{3,4}([A-Z][a-z]+[A-Z]?[a-z]+).csv'

    match = re.findall(pattern, file_name)

    if match:
        return match[0].lower()
    else:
        raise ValueError('File name does not match the expected pattern')
