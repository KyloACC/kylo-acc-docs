import csv
import sys

def moving_average(lap_times):
	num_laps = len(lap_times)
	moving_averages = dict()

	for i in range(num_laps):
		if lap_times[i] is None:
			moving_averages[i] = None
			continue

		if i < 2:
			valid_lap_times = [lt for lt in lap_times[:i + 2] if lt is not None]
			avg = sum(valid_lap_times) / len(valid_lap_times)
		elif i >= num_laps - 2:
			valid_lap_times = [lt for lt in lap_times[i - 2:] if lt is not None]
			avg = sum(valid_lap_times) / len(valid_lap_times)
		else:
			valid_lap_times = [lt for lt in lap_times[i - 2:i + 3] if lt is not None]
			avg = sum(valid_lap_times) / len(valid_lap_times)

		moving_averages[i] = avg
		#print(str(i) + ": " + str(avg))

	return moving_averages



def average_laptime(lap_times):
	num_laps = len(lap_times)
	if num_laps < 9:
		lap_times = lap_times[num_laps:]
	laptimes_sum = 0
	for a in lap_times:
		laptimes_sum = laptimes_sum + a
	average_laptime_data = laptimes_sum / num_laps
	return average_laptime_data


def process_lap_times(input_file):
	lap_times = []
	lap_numbers = []

	with open(input_file, 'r') as file:
		reader = csv.reader(file)
		next(reader)  # Skip header row
		x = 0
		for row in reader:
			#print(str(x))
			x = x+1
			driver = row[2].strip('"').strip(" ").strip('"')
			minutes, seconds = row[1].strip().split(":")
			minutes = minutes.replace('"', "")
			seconds = seconds.replace('"', "")

			lap_time = int(minutes) * 60 + float(seconds)
			lap_times.append(lap_time)
			lap_numbers.append(x)
		#for a in lap_numbers:
			#print(str(a))	

	avg_lap = average_laptime(lap_times)

	lap_times2 = []
	lap_numbers2 = []
	for x in range(len(lap_times)):
		if lap_times[x] < avg_lap:
			lap_times2.append(lap_times[x])
			lap_numbers2.append(lap_numbers[x])
		else:
			lap_times2.append(None)
			lap_numbers2.append(lap_numbers[x])

	#for x in range(len(lap_times2)):
		#print(str(lap_numbers2[x]) + ": " + str(lap_times2[x]))
		
	moving_averages = moving_average(lap_times2)		

	print('"Lap", "laptime", "driver"')

	with open(input_file, 'r') as file:
		next(file)  # Skip header row
			
		x = 0
		for lap, laptime in moving_averages.items():
			if laptime is not None:
				minutes = int(laptime / 60)
				seconds = "{:.4f}".format(round(laptime - minutes * 60, 4))	
				print(f'"{lap}", "{minutes}:{seconds}", "{driver}"')
			else:
				print(f'"{lap}", "", "{driver}"')
				
	#print("Moving average lap times written to", output_file)

input_file = "output_T1_" + sys.argv[1] + ".txt"

process_lap_times(input_file)
