import csv

# Read your CSV file
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)
    
# Use your data
print(f"Loaded {len(data)} rows")
for row in data:
    print(row)
