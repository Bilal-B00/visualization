from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.line_graph import linegraph

from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
from dash import dcc


if __name__ == '__main__':
    # Create data
    df = pd.read_csv('C:/Users/Tychon Bos/Google Drive/CSAI/Visualization/data.csv')

    # Instantiate custom views
    #scatterplot1 = Scatterplot("Scatterplot 1", 'male', 'accident_count', df)
    #scatterplot2 = Scatterplot("Scatterplot 2", 'male', 'accident_count', df)
    line = linegraph('accident_index', 'accident_year_x', [1,2,3,4], 'sex_of_driver' ,df)
   
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
                children=[dcc.Graph(figure = line, id='grpah')
                ],
            ),
        ],
    )
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

    app.run_server(debug=False, dev_tools_ui=False)