import pandas as pd
import plotly.express as px
df = pd.read_csv("laguna seca lap times.csv")
fig = px.box(df, y="laptime", x="car",
	notched=True,
	title="Laguna Seca LFM Lap Times")
fig.show()