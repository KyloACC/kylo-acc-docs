import csv
from datetime import datetime, timedelta

def parse_lap_time(lap_time):
    # Convert lap time from string format (MM:SS.sss) to timedelta
    try:
        lap_time = datetime.strptime(lap_time, '%M:%S.%f')
        minutes = lap_time.minute
        seconds = lap_time.second
        milliseconds = lap_time.microsecond // 1000
        return timedelta(minutes=minutes, seconds=seconds, milliseconds=milliseconds)
    except ValueError:
        return None

def format_lap_time(lap_time):
    # Convert lap time from timedelta to string format (MM:SS.sss)
    milliseconds = lap_time.microseconds // 1000
    return lap_time.strftime('%M:%S.') + str(milliseconds).zfill(3)

def calculate_stints(lap_times):
    stints = []
    current_stint = 1
    average_lap_time = parse_lap_time(lap_times[0][2])

    for i in range(1, len(lap_times)):
        lap_number = int(lap_times[i][0])
        lap_time = parse_lap_time(lap_times[i][2])
        
        if lap_time is None:
            continue
        
        rolling_average = (average_lap_time * (lap_number - 1) + lap_time) / lap_number

        if lap_time > average_lap_time + (0.1 * average_lap_time):
            stints.append((lap_number, current_stint))
            current_stint += 1
            average_lap_time = lap_time
        else:
            average_lap_time = rolling_average

    stints.append((lap_number + 1, current_stint))  # Include the last lap in the final stint
    return stints


def main():
    lap_times = []

    with open('output.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            lap_times.append(row)

    stints = calculate_stints(lap_times)

    with open('lap_times_with_stints.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['LapNumber', 'LapTime', 'Stint'])

        for lap in lap_times:
            lap_number = lap[0]
            lap_time = parse_lap_time(lap[2])
            
            if lap_time is None:
                continue
            
            stint = next((stint for lap_num, stint in stints if lap_num == int(lap_number)), 0)
            writer.writerow([lap_number, format_lap_time(lap_time), stint])


if __name__ == '__main__':
    main()
