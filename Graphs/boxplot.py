# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

# Read csv file
df = pd.read_csv(sys.argv[1] + ".csv")

# Change resolution
fig, ax = plt.subplots(figsize=(int(sys.argv[5]), 4.5)) 

# Filter out lap times that are 10000ms slower than the stint average
df = df[df["laptime_in_ms"] <= df.groupby("stint")["laptime_in_ms"].transform("mean") + int(float(sys.argv[4])*1000)]

# Create a new column with the x axis labels
df["x_label"] = df["driver"] + " - Stint " + df["stint"].astype(str) + " - " + df.groupby("stint")["lap"].transform("count").astype(str) + " laps"

# Create a box plot with x as x_label and y as laptime_in_ms
sns.boxplot(data=df, x="x_label", y="laptime_in_ms")

# Add a title that you can change yourself
plt.title(sys.argv[3])

# Rotate the x axis labels for better readability
plt.xticks(rotation=int(sys.argv[5]), fontsize=8) 

# Show the plot
plt.show()
plt.savefig(sys.argv[2] + "_boxplot.png", dpi=500)