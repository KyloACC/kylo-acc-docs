import pandas as pd
import plotly.express as px
df = pd.read_csv("Paul Ricard lap times.csv")
fig = px.box(df, y="laptime", x="car",
	notched=True,
	title="Paul Ricard LFM Lap Times")
fig.show()