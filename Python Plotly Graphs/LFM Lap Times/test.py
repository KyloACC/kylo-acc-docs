import pandas as pd
import plotly.express as px
df = pd.read_csv("suzuka lap times.csv")
fig = px.box(df, y="laptime", x="car",
	notched=True,
	title="Suzuka LFM Lap Times")
fig.show()