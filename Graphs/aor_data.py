import matplotlib.pyplot as plt

# Read the lap time data from the file
data_file = "data.txt"
data = []
with open(data_file, "r") as file:
    next(file)  # Skip the first line (headers)
    for line in file:
        line = line.strip().split(",")
        data.append(line)

# Create lists to store lap numbers and filtered lap times
lap_numbers = []
filtered_lap_times = []

# Iterate over the data and calculate the average and filter anomalies
for i in range(len(data)):
    if i >= 2:
        # Split the lap time into minutes, seconds, and tenthousands of a second
        laptime_parts = data[i][1].strip().strip('"').split(":")
        laptime_parts[1] = laptime_parts[1].strip().strip('"').split(".")
        minutes = float(laptime_parts[0])
        seconds = float(laptime_parts[1][0])
        tenthousands = float(laptime_parts[1][1])
        
        #print(str(minutes) + " " + str(seconds) + " " + str(tenthousands))

        # Convert lap time to milliseconds
        laptime_ms = (minutes * 60 * 1000) + (seconds * 1000) + (tenthousands / 10)

        # Calculate the average of the last 3 lap times in milliseconds
        laptime_1 = data[i - 2][1].strip().strip('"').split(":")
        laptime_1[1] = laptime_1[1].strip().strip('"').split(".")
        minutes_1 = float(laptime_1[0])
        seconds_1 = float(laptime_1[1][0])
        tenthousands_1 = float(laptime_1[1][1])
        laptime_ms_1 = (minutes_1 * 60 * 1000) + (seconds_1 * 1000) + (tenthousands_1 / 10)

        laptime_2 = data[i - 1][1].strip().strip('"').split(":")
        laptime_2[1] = laptime_2[1].strip().strip('"').split(".")
        minutes_2 = float(laptime_2[0])
        seconds_2 = float(laptime_2[1][0])
        tenthousands_2 = float(laptime_2[1][1])
        laptime_ms_2 = (minutes_2 * 60 * 1000) + (seconds_2 * 1000) + (tenthousands_2 / 10)

        average = (laptime_ms_1 + laptime_ms_2 + laptime_ms) / 3
        lap_numbers.append(int(data[i][0].strip('"')))
        filtered_lap_times.append(average)
        
# Filter out lap times that are 5% higher than the average
lap_numbers_filtered = []
filtered_lap_times_filtered = []
for lap, lap_time in zip(lap_numbers, filtered_lap_times):
    if lap_time <= average * 1.02:
        lap_numbers_filtered.append(lap)
        filtered_lap_times_filtered.append(lap_time)

# Plot the lap times on a graph
plt.plot(lap_numbers_filtered, filtered_lap_times_filtered, marker='')
plt.xlabel('Lap')
plt.ylabel('Lap Time (milliseconds)')
plt.title('Filtered Lap Times')
# Save the figure as a PNG file
plt.savefig('lap_times_plot.png', dpi=300)
