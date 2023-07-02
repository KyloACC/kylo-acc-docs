import sys

# Read the input file
with open("input_" + sys.argv[1] + ".txt", 'r') as file:
    lines = file.readlines()

formatted_lines = []

# Extract the driver name from the second line
driver = lines[1].strip()

formatted_lines.append('"Lap", "laptime", "driver"')

# Iterate over the lap data lines and reformat the data
for line in lines[2:]:
    line = line.strip()
    lap_data = line.split(',')
    lap = lap_data[0].strip()
    laptime = lap_data[4].strip()

    # Create the formatted line
    formatted_line = f'{lap}, {laptime}, {driver}'
    formatted_lines.append(formatted_line)

# Write the formatted data to a new file
with open("output_" + sys.argv[1] + ".txt", 'w') as file:
    file.write('\n'.join(formatted_lines))
