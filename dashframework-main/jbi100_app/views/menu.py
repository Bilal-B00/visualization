from dash import dcc, html
from ..config import color_list1, color_list2


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Visualizaton tool group 34"),

            html.Div(
                id="intro",
                children="Data contains accidents in the UK",
            ),
        ],
    )


def generate_control_card():
    """

    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.Label("Year of population pyramid"),
            dcc.Dropdown(
            html.Label("Line graph"),
            dcc.Dropdown(
                id="LineGraph",
                options=[{"label": i, "value": i} for i in ['Male', 'Female', 'Other', 'Total', 'All', 'Male and Female', 'Male and Other', 'Female and Other', 'Male and Total', 'Female and Total', 'Total and Other']], 
                value='Total', searchable=True, placeholder='Please select...', clearable=True
                
            ),
                id="year-of-population-pyramid",
                options=[{"label": i, "value": i} for i in range(2016, 2021) ],
                value = 2016
            )
        ], style={"textAlign": "float-left"}
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]


