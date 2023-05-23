# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

# Read csv file
df = pd.read_csv(sys.argv[1] + ".csv")

# Filter out lap times that are 10000ms slower than the stint average
df = df[df["laptime_in_ms"] <= df.groupby("stint")["laptime_in_ms"].transform("mean") + int(float(sys.argv[3])*1000)]

# Create a violin plot with hue as stint and color as driver
sns.violinplot(data=df, x="stint", y="laptime_in_ms", hue="driver", palette="Set2", cut=0)

# Add the name of the driver and the amount of laps somewhere
plt.title(f"{df['driver'].iloc[0]} - {len(df)} laps")

# Add a title that you can change yourself
plt.title(sys.argv[4])

# Show the plot
plt.show()

plt.savefig(sys.argv[2] + "_violins.png", dpi=500)