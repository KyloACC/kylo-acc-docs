import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("imola lap times lfm.csv")

fig = go.Figure()

Cars = ['BMW M4', 'Aston Martin V8', 'Porsche 2019', 'Honda Evo', 'Ferrari Evo', 'Mercedes 2020', 'Bentley 2018', 'McLaren 720S', 'Ferrari', 'Porsche Cayman', 'Audi Evo 2', 'Lexus', 'Nissan 2018', 'Lambo Evo', 'Audi Evo', 'Mercedes 2015', 'Aston Martin V12', 'Jaguar', 'Porsche GT3 2018']

for car in Cars:
    fig.add_trace(go.Violin(x=df['Car'][df['Car'] == car],
                            y=df['laptime'][df['Car'] == car],
                            spanmode="hard",
                            width=0,
                            name=car,
                            box_visible=True,
                            meanline_visible=True)
    )

fig.show()