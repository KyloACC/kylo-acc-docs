import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("Track Ratings.csv")

fig = go.Figure()

tracks = ['Autodromo Enzo e Dino Ferrari','Barcelona','Brands Hatch','Donington Park','Hungaroring','Kyalami','Laguna Seca','Misano','Monza','Mount Panorama','Nürburgring','Oulton Park','Paul Ricard','Silverstone','Snetterton Circuit','Spa-Francorchamps','Suzuka','Zandvoort','Zolder','Average']

for track in tracks:
    fig.add_trace(go.Violin(x=df['track'][df['track'] == track],
                            y=df['ranking'][df['track'] == track],
                            spanmode="hard",
                            width=0,
                            name=track,
                            box_visible=True,
                            meanline_visible=True))
fig.show()

