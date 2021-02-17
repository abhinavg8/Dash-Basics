import datetime
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df = df[['continent', 'country', 'pop', 'lifeExp']]  # prune columns for example
df['Mock Date'] = [
    datetime.datetime(2020, 1, 1, 0, 0, 0) + i * datetime.timedelta(hours=13)
    for i in range(len(df))
]
Continents = df.continent.unique()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in Continents],
        value=Continents[0],
        clearable=False,
    ),
    dcc.Graph(id="bar-chart"),
])

@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown", "value")])

def update_bar_chart(continent):
    mask = df["continent"] == continent
    fig = px.bar(df[mask], x="country", y="pop",
                 )
    return fig

app.run_server(debug=True)