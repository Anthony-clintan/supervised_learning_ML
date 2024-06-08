import csv

# Your dictionary
dict_data = {
    "Name": ["Sam", "Dean", "Castiel"],
    "Age": [30, 35, 'Unknown'],
    "Occupation": ["Hunter", "Hunter", "Angel"]
}

# Name of csv file where data should be saved
csv_file = "dict_data.csv"

# Writing to csv file
with open(csv_file, 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=dict_data.keys())
    writer.writeheader()
    writer.writerow(dict_data)