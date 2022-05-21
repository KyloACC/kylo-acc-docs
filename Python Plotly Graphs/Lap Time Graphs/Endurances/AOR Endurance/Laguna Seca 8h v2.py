import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("Laguna Seca 8h.csv")

fig = go.Figure()

drivers = ['Hubert Szymański','Luca Ziege','Ryan Cooper']

for driver in drivers:
    fig.add_trace(go.Violin(x=df['driver'][ df['stint'] == 1 ],
                            y=df['time in seconds'][ df['stint'] == 1 ],
                            legendgroup='Yes', scalegroup='Yes', name='Stint 1',
                            side='negative',
                            line_color='yellow')
                 )
    fig.add_trace(go.Violin(x=df['driver'][ df['stint'] == 2 ],
                            y=df['time in seconds'][ df['stint'] == 2 ],
                            legendgroup='No', scalegroup='No', name='Stint 2',
                            side='positive',
                            line_color='Purple')
                 )
    fig.add_trace(go.Violin(x=df['driver'][ df['stint'] == 3 ],
                            y=df['time in seconds'][ df['stint'] == 3 ],
                            legendgroup='No', scalegroup='No', name='Stint 3',
                            side='negative',
                            line_color='blue')
                 )
    fig.add_trace(go.Violin(x=df['driver'][ df['stint'] == 4 ],
                            y=df['time in seconds'][ df['stint'] == 4 ],
                            legendgroup='No', scalegroup='No', name='Stint 4',
                            side='positive',
                            line_color='Gold')
                 )
fig.update_traces(meanline_visible=True)
fig.update_layout(violingap=0, violinmode='overlay')
fig.show()