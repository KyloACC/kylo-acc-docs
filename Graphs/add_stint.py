import pandas as pd
import sys

# Load data from CSV file
df = pd.read_csv(sys.argv[1])

# Convert lap time column to milliseconds
df['laptime_in_ms'] = pd.to_timedelta('00:' + df['laptime']).dt.total_seconds() * 1000

# Add stint column based on lap times
min_laptime = df['laptime_in_ms'].min()
df['stint'] = ((df['laptime_in_ms'] - min_laptime) > 50000).cumsum() + 1

# Convert lap time back to string format 'mm:ss.xxx'
df['laptime'] = pd.to_datetime(df['laptime_in_ms'], unit='ms').dt.strftime('%M:%S.%f')

# Write result to CSV file
df.to_csv(sys.argv[2], index=False)
