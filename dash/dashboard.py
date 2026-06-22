import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dash import Dash, html, dcc
import plotly.graph_objs as go
import plotly.express as px

# 1. Load data and filter for a specific year so the plot is readable
df = px.data.gapminder()
df_2007 = df[df['year'] == 2007]

app = Dash(__name__)

app.layout = html.Div([
    # Header Row
    html.Div(children=[
        html.H1("My First Dashboard", style={'color': 'red', 'textAlign': 'center'})
    ], style={'border': '1px solid black', 'float': 'left', 'width': '100%', 'height': '60px'}),
    
    # Left Graph Column
    html.Div(children=[
        dcc.Graph(
            id='scatter-plot',
            figure=px.scatter(
                df_2007, 
                x='pop', 
                y='gdpPercap', 
                hover_name='country',
                log_x=True, # Optional: Makes population gaps easier to see
                title='GDP vs Population (2007)'
            )
        )
    ], style={'border': '1px solid black', 'float': 'left', 'width': '49%', 'height': '450px'}),
    
    # Right Empty Column (Ready for your next chart)
    html.Div(children=[
            dcc.Graph(
                id='box-plot1',
                figure=px.box(
                    df_2007,
                    x='continent',
                    y='lifeExp',
                    title='Life Expectancy by Continent(2007)'
                )
            )
        ],
        style={'border': '1px solid black', 'float': 'right', 'width': '49%', 'height': '450px'}
    ),
])

if __name__ == '__main__':
    app.run(debug=True)