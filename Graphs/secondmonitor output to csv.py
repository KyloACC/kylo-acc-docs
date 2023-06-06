import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    laps = data

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['LapNumber', '', 'laptime'])

        for lap in laps:
            lap_number = lap['LapNumber']
            lap_time = lap['LapTime'][3:-4]

            writer.writerow([lap_number, '', lap_time])

    print(f"CSV file '{csv_file}' has been created successfully.")

# Usage
json_file_path = 'input.json'
csv_file_path = 'output.csv'

json_to_csv(json_file_path, csv_file_path)
