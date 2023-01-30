import pandas as pd
import plotly.express as px
df = pd.read_csv("Paul Ricard lap times v3.csv")
fig = px.box(df, y="laptime in seconds", x="car",
	notched=True,
	title="Paul Ricard LFM Lap Times")
fig.show()