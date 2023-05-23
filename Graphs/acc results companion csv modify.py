import sys
# Open the input file
with open(sys.argv[1], "r") as f:

    # Skip the first line
    next(f)

    # Get the header row
    header = next(f).strip().split(",")

    # Find the indexes of the columns we want
    lap_index = header.index('"Lap"')
    driver_index = header.index('"Driver"')
    laptime_index = header.index('"Lap Time"')

    # Open the output file
    with open("output_file.txt", "w") as out_file:

        # Write the new header row
        out_file.write("lap,driver,laptime\n")

        # Loop over the remaining lines in the input file
        for line in f:

            # Split the line into columns
            columns = line.strip().split(",")

            # Extract the data we want
            lap = columns[lap_index]
            driver = columns[driver_index]
            laptime = columns[laptime_index]

            # Write the new line to the output file
            out_file.write("{},{},{}\n".format(lap, driver, laptime))
