from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Scatterplot
from jbi100_app.views.population_pyramid import populationPyramid
from jbi100_app.views.histogram import histogram
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from dash import dcc, html

from dash import html
import plotly.express as px
from dash.dependencies import Input, Output


if __name__ == '__main__':
    # Create data
    df = px.data.iris()
    df_2 = pd.read_csv('C:/Users/Bilal/Downloads/data.csv')

    # Instantiate custom views
    pyramid = populationPyramid("sex_of_driver", "age_band_of_driver", df_2, 2016)
    hist1 = histogram('age_band_of_driver', '', 0, "Age Band", df_2)
    hist2 = histogram('vehicle_type', 'age_band_of_driver', 9, 'Vehicle Type', df_2)
    hist3 = histogram("sex_of_driver", "age_band_of_driver", 9, "Sex of Driver", df_2)

    app.layout = html.Div(
        id="app-container",
        children=[
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=make_menu_layout()
            ),

            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children=[
                    dcc.Graph(figure = pyramid, id='pyramid'),
                    html.Br(),
                    html.Center(html.H1(id='vehicle_title')),
                    html.Div( children = [
                            html.Br(),
                            html.Div(dcc.Graph(figure = hist1, id='hist1', style = {'width':'333px'}), style = {'display':'inline-block'}),
                            html.Div(dcc.Graph(figure = hist2, id='hist2', style = {'width':'333px'}), style = {'display':'inline-block'}),
                            html.Div(dcc.Graph(figure = hist3, id='hist3', style = {'width':'333px'}), style = {'display':'inline-block'})],
                            style = {'wdith':'100%', 'display':'inline-block'}),
                            ]
            ),
        ],
    )

    # Define interactions
    @app.callback(
        Output("pyramid", "figure"),
        Input("year-of-population-pyramid", "value"))
    def update_populationpyramid(value):
        return populationPyramid("sex_of_driver", "age_band_of_driver", df_2, value)
    @app.callback(
            [Output("hist2", "figure"),
             Output("vehicle_title", "children"),
             Output("hist3", "figure")],
            Input("hist1", "clickData"))
    def update_hist(clickData):
        return histogram('vehicle_type', 'age_band_of_driver', clickData["points"][0]["x"], "Vehicle Type", df_2), 'Age Band Selected: {}'.format(clickData["points"][0]["x"]), histogram('sex_of_driver', 'age_band_of_driver', clickData["points"][0]["x"], "Sex of Driver", df_2) 

    


    app.run_server(debug=False, dev_tools_ui=False)