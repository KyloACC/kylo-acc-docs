import matplotlib.pyplot as plt
import glob
import sys
import re

minimum_laps = 0
maximum_laps = 0

minimum_laptime = float()
maximum_laptime = float()

file_pattern = "output_*.txt"
file_list = glob.glob(file_pattern)

datafiles = []
for file_name in file_list:
    # Extract the "xxx" part from the file name
    file_number = file_name[len("output_"):-len(".txt")]
    
    # Check if the file number consists of only alphabetic characters
    if re.match(r"^[A-Za-z]+$", file_number):
        datafiles.append(file_number)

print(datafiles)

fig = plt.figure(figsize=(15, 5))

# Read the lap time data from the file
for datafile in datafiles:
	data = []
	with open("output_" + datafile + ".txt", "r") as file:
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
			laptime_ms = (minutes * 60) + (seconds) + (tenthousands / 10000)

			# Calculate the average of the last 3 lap times in milliseconds
			laptime_1 = data[i - 2][1].strip().strip('"').split(":")
			laptime_1[1] = laptime_1[1].strip().strip('"').split(".")
			minutes_1 = float(laptime_1[0])
			seconds_1 = float(laptime_1[1][0])
			tenthousands_1 = float(laptime_1[1][1])
			laptime_ms_1 = (minutes_1 * 60 ) + (seconds_1) + (tenthousands_1 / 10000)

			laptime_2 = data[i - 1][1].strip().strip('"').split(":")
			laptime_2[1] = laptime_2[1].strip().strip('"').split(".")
			minutes_2 = float(laptime_2[0])
			seconds_2 = float(laptime_2[1][0])
			tenthousands_2 = float(laptime_2[1][1])
			laptime_ms_2 = (minutes_2 * 60) + (seconds_2) + (tenthousands_2 / 10000)

			average = (laptime_ms_1 + laptime_ms_2 + laptime_ms) / 3
			lap_numbers.append(int(data[i][0].strip('"')))
			filtered_lap_times.append(average)
			
	# Filter out lap times that are 5% higher than the average
	sum = 0
	for laps in filtered_lap_times:
		sum += laps
	average_laps = sum / len(filtered_lap_times)
	lap_numbers_filtered = []
	filtered_lap_times_filtered = []
	for lap, lap_time in zip(lap_numbers, filtered_lap_times):
		if lap_time <= average_laps * 1.01:
			lap_numbers_filtered.append(lap)
			filtered_lap_times_filtered.append(lap_time)

	if(min(lap_numbers_filtered) < minimum_laps):
		minimum_laps = min(lap_numbers_filtered)
	if(max(lap_numbers_filtered) > minimum_laps):
		maximum_laps = max(lap_numbers_filtered)
	if(minimum_laptime == 0.0):
		minimum_laptime = min(filtered_lap_times_filtered)
	if(min(filtered_lap_times_filtered) < minimum_laptime):
		minimum_laptime = min(filtered_lap_times_filtered)
	if(max(filtered_lap_times_filtered) > maximum_laptime):
		maximum_laptime = max(filtered_lap_times_filtered)
	print(str(max(filtered_lap_times_filtered)))
	

	

	# Plot the lap times on a graph
	plt.plot(lap_numbers_filtered, filtered_lap_times_filtered, marker='', label=datafile)

# Set the plot limits to exclude the NaN values
maximum_laptime = maximum_laptime*(1-float(sys.argv[2])*0.01)
print(str(minimum_laptime) + " " + str(maximum_laptime))
plt.xlim(minimum_laps, maximum_laps)
plt.ylim(minimum_laptime, maximum_laptime)
plt.xlabel('Lap')
plt.ylabel('Lap Time (seconds)')
plt.title(sys.argv[1])
# Display the legend
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# Save the figure as a PNG file

plt.savefig("AOR_T2_lap_times_plot_" + sys.argv[1] + ".png", dpi=1000)
