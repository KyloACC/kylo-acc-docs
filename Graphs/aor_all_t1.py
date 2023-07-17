import matplotlib.pyplot as plt
import glob
import sys
import os

fig = plt.figure(figsize=(15, 5))

min_laptime = float('inf')
max_laptime = float('-inf')

file_pattern = "output2_T1_*.txt"
file_list = glob.glob(file_pattern)
for file_name in file_list:
	datafile = file_name[len("output2_T1_"):-len(".txt")]
	lap_numbers = []
	lap_times = []

	with open(file_name, "r") as file:
		if os.path.exists(file_name) and os.path.getsize(file_name) == 0:
			continue  # Continue with the next iteration or skip the code block
		next(file)  # Skip the first line (headers)
		for line in file:
			line = line.strip().split(",")
			lap_number = int(line[0].strip('"'))
			#print(line[1])
			if line[1] == ' ""':
				lap_time = None
			else:
				minutes, seconds = line[1].strip().split(":")
				minutes = minutes.replace('"', "")
				seconds = seconds.replace('"', "")
				lap_time = int(minutes) * 60 + float(seconds)

			lap_numbers.append(lap_number)
			lap_times.append(lap_time)
			
			# Update minimum and maximum lap times
			if lap_time is not None:

				min_laptime = min(min_laptime, lap_time)
				max_laptime = max(max_laptime, lap_time)
		#for a in lap_times:
			#print(str(a))

	plt.plot(lap_numbers, lap_times, marker='', label=datafile)

# Set the y-axis limits based on the minimum and maximum lap times
plt.ylim(min_laptime, max_laptime)
plt.xlabel('Lap')
plt.ylabel('Lap Time (seconds)')
plt.title(sys.argv[1])
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("AOR_T1_lap_times_plot_" + sys.argv[1] + ".png", dpi=1000)
