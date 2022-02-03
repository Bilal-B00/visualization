from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout

from jbi100_app.views.line_graph import linegraph
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
import pandas as pd
from dash import dcc

from urllib.request import urlopen
import json                                                   #necessary library
with urlopen('https://raw.githubusercontent.com/martinjc/UK-GeoJSON/master/json/administrative/gb/lad.json') as response:
    district = json.load(response) #opens the Geojson file necessary for the plot from the raw Json file. 
                                   #Json file is made by martinjc and can be found on https://martinjc.github.io/UK-GeoJSON/


if __name__ == '__main__':
    # Create data

    df = pd.read_csv('data.csv')
    line = linegraph('accident_index', 'accident_year_x', [1,2,3,4], 'sex_of_driver' ,df)
    
    df_map = pd.read_csv('map.csv', dtype={"LAD13CD": str})            # opens the csv file in the directory

    # Instantiate custom views
    pyramid = populationPyramid("sex_of_driver", "age_band_of_driver", df, 2016)
    hist1 = histogram('age_band_of_driver', '', 0, "Age Band", df)
    hist2 = histogram('vehicle_type', 'age_band_of_driver', 9, 'Vehicle Type', df)
    hist3 = histogram("sex_of_driver", "age_band_of_driver", 9, "Sex of Driver", df)
    
    map = px.choropleth(df_map , geojson = district,           # Dataset and geojson are loaded
                    featureidkey = "properties.LAD13NM",       # Featurekey from the dataset
                    locations = df_map["LAD13NM"],             # Uses the featurekey to build the locations from the Geojson file
                    color='total_accident_district',           # Assigns the colormap to the chosen attribute
                    range_color=(0, 4000),                     # Range for which the color scale are applied
                    scope = 'europe',                          # Scope for base map
                    color_continuous_scale="blues",            # Colourmap choice
                    title = "choropleth map UK accidents"                                               
                    
)

    map.update_geos(fitbounds="locations", visible=False)
    map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


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
                            style = {'width':'100%', 'display':'inline-block'}),
                            html.Br(),
                            dcc.Graph(figure = line, id='grpah'),
                            html.Br(),
                            dcc.Graph(figure = map)
                            ]

            ),
        ],
    )
    
    @app.callback(
        Output("pyramid", "figure"),
        Input("year-of-population-pyramid", "value"))
    def update_populationpyramid(value):
        return populationPyramid("sex_of_driver", "age_band_of_driver", df, value)
    @app.callback(
            [Output("hist2", "figure"),
             Output("vehicle_title", "children"),
             Output("hist3", "figure")],
            Input("hist1", "clickData"))
    def update_hist(clickData):
        return histogram('vehicle_type', 'age_band_of_driver', clickData["points"][0]["x"], "Vehicle Type", df), 'Age Band Selected: {}'.format(clickData["points"][0]["x"]), histogram('sex_of_driver', 'age_band_of_driver', clickData["points"][0]["x"], "Sex of Driver", df) 
    
    @app.callback(
        Output(component_id = 'grpah', component_property = 'figure' ),
        Input(component_id = 'LineGraph' , component_property = 'value' ))
    
    def update(value):
        if value == 'Male':
            return linegraph('accident_index', 'accident_year_x', [1], 'sex_of_driver' ,df)
        elif value == 'Female':
            return linegraph('accident_index', 'accident_year_x', [2], 'sex_of_driver' ,df)
        elif value == 'Other':
            return linegraph('accident_index', 'accident_year_x', [3], 'sex_of_driver' ,df)
        elif value == 'Total':
            return linegraph('accident_index', 'accident_year_x', [4], 'sex_of_driver' ,df)
        elif value == 'All':
            return linegraph('accident_index', 'accident_year_x', [1,2,3,4], 'sex_of_driver' ,df)
        elif value == 'Male and Female':
            return linegraph('accident_index', 'accident_year_x', [1,2], 'sex_of_driver' ,df)
        elif value == 'Male and Other':
            return linegraph('accident_index', 'accident_year_x', [1,3], 'sex_of_driver' ,df)
        elif value == 'Male and Total':
            return linegraph('accident_index', 'accident_year_x', [1,4], 'sex_of_driver' ,df)
        elif value == 'Female and Total':
            return linegraph('accident_index', 'accident_year_x', [2,4], 'sex_of_driver' ,df)
        elif value == 'Female and Other':
            return linegraph('accident_index', 'accident_year_x', [2, 3], 'sex_of_driver' ,df)
        elif value == 'Total and Other':
            return linegraph('accident_index', 'accident_year_x', [3,4], 'sex_of_driver' ,df)
   

    app.run_server(debug=False, dev_tools_ui=False)
