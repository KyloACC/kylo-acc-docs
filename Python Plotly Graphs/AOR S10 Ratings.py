import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("AOR S10 Ratings.csv")

fig = go.Figure()

Drivers = ['Foch','BGS','Schubert','Jardier','Geert Fischer','Harry Phillips','One Ko','Flicker','Riba','Kylo','Arkensyel','Harley','Ryan','Geg','Buras','Dimitri Slow']

for driver in Drivers:
    fig.add_trace(go.Violin(x=df['Driver'][df['Driver'] == driver],
                            y=df['Position'][df['Driver'] == driver],
                            spanmode="hard",
                            width=0,
                            name=driver,
                            box_visible=True,
                            meanline_visible=True)
    )

fig.show()