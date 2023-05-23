import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# Load the CSV file into a pandas DataFrame
data = pd.read_csv(sys.argv[1] + ".csv")

# Get a list of unique stints
stints = data["stint"].unique()

# Generate a list of colors to use for the stints
colors = plt.cm.Set1(np.linspace(0, 1, len(stints)))

# Create a new figure and axis for the plot
fig, ax = plt.subplots()

# Loop over each stint and plot the lap times for that stint, filtering out outliers
for i, stint in enumerate(stints):
    stint_data = data[data["stint"] == stint]
    median_laptime = stint_data["laptime_in_ms"].median()
    filtered_data = stint_data[stint_data["laptime_in_ms"] <= median_laptime + int(float(sys.argv[3])*1000)]
    driver = filtered_data["driver"].iloc[0]
    ax.plot(filtered_data["lap"], filtered_data["laptime_in_ms"]/1000, color=colors[i], label=f"Stint {stint} ({len(filtered_data)} laps) - {driver}")

# Add labels and a legend to the plot
ax.set_xlabel("Lap")
ax.set_ylabel("Lap Time (s)")
ax.legend()

# Add a title that you can change yourself
plt.title(sys.argv[4])

# Display the plot
plt.show()
plt.savefig(sys.argv[2] + "_linechart.png", dpi=500)
