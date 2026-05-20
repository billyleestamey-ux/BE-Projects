# Read the CSV file line by line
with open('data.csv', 'r') as file:
    lines = file.readlines()
    
    # First line is headers
    headers = lines[0].strip().split(',')
    print(f"Columns: {headers}")
    
    # Rest are data rows
    for line in lines[1:]:
        values = line.strip().split(',')
        print(f"Row: {values}")
