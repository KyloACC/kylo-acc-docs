import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("barcelona_rdc_laptimes_stints.csv")

fig = go.Figure()

drivers = ['Kylo Stint 1','Schubert Stint 1','Flicker Stint 1','Kylo Stint 2','Flicker Stint 2','Kylo Stint 3','Flicker Stint 3','Schubert Stint 2','Kylo Stint 4','Schubert Stint 3','Kylo Stint 5','Kylo Stint 6']

for driver in drivers:
    fig.add_trace(go.Violin(x=df['driver'][df['driver'] == driver],
                            y=df['time in seconds'][df['driver'] == driver],
                            spanmode="hard",
                            width=0,
                            name=driver,
                            box_visible=True,
                            meanline_visible=True))

fig.show()