import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("laguna seca lap times.csv")

fig = go.Figure()

cars = ['Audi Evo 2','Aston Martin V8', 'Bentley 2018', 'BMW M4','BMW M6','Ferrari Evo','Honda Evo','Lambo Evo','Lexus','McLaren 720S','Porsche 2019']

for cars in cars:
    fig.add_trace(go.Violin(x=df['cars'][df['cars'] == cars],
                            y=df['laptime'][df['cars'] == cars],
                            spanmode="hard",
                            width=0,
                            name=cars,
                            box_visible=True,
                            meanline_visible=True))
fig.show()

