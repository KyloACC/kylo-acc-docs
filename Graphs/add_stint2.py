import pandas as pd
import sys

# Load data from CSV file
df = pd.read_csv(sys.argv[1])

# Split laptime into minutes, seconds, and milliseconds
time_parts = df['laptime'].str.split(':', expand=True)
minutes = time_parts[0].astype(int)
seconds = time_parts[1].str.split('.', expand=True)[0].astype(int)
milliseconds = time_parts[1].str.split('.', expand=True)[1].astype(int)

# Convert laptime to milliseconds
df['laptime'] = minutes * 60 * 1000 + seconds * 1000 + milliseconds

# Add stint column based on lap times
min_laptime = df['laptime'].min()
df['stint'] = ((df['laptime'] - min_laptime) > 50000).cumsum() + 1

# Write result to CSV file
df.to_csv(sys.argv[2], index=False)
