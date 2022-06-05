import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("barcelona_rdc_laptimes.csv")

fig = go.Figure()

drivers = ['Schubert','Kylo','Flicker']

for driver in drivers:
    fig.add_trace(go.Violin(x=df['driver'][df['driver'] == driver],
                            y=df['time in seconds'][df['driver'] == driver],
                            spanmode="hard",
                            width=0,
                            name=driver,
                            box_visible=True,
                            meanline_visible=True))

fig.show()