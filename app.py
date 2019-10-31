import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data_path = 'data/Mean_Temp_IMD_2017.csv'
df = pd.read_csv(data_path)
df = df.set_index('YEAR')

time_durations = df.columns

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='time_durs',
                options=[{'label': i, 'value': i}
                         for i in time_durations],
                value='Month'
            )
        ],
            style={'width': '48%', 'display': 'inline-block'})
    ]),
    dcc.Graph(id='indicator-graphic')
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('time_durs', 'value')])
def update_graph(month):
    dff = df[month]

    return {
        'data': [go.Scatter(
            x=list(dff.index),
            y=dff.values,
            mode='lines+markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)'
            }],
            'yaxis': {'type': 'linear'},
            'xaxis': {'showgrid': False}
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)
