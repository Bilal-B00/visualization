import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from dash import dcc, html

# initialization of population pyramid function
def populationPyramid(sex_col, age_band_col, df, year):
    # initialize figure objects with two columns
    fig = make_subplots( rows = 1, cols = 2, horizontal_spacing = 0 )
            
    age_band = np.sort( df[ age_band_col ].unique() )
            
    men_bin = []
    women_bin = []
    
    # calculate totale accidents of males and females per age band        
    for i in age_band:
        if i == -1:
            continue
        else:
            men_bin.append( df[ ( df[ sex_col ] == 1 ) & ( df[ age_band_col ]  == i ) & ( df[ 'accident_year_x' ] == year ) ].shape[0] )
            women_bin.append( df[ ( df[ sex_col ] == 2 ) & ( df[ age_band_col ]  == i ) & ( df[ 'accident_year_x' ] == year ) ].shape[0] )
                    
    men_bin = np.array( men_bin )
    women_bin = np.array( women_bin )
    
    # horizantal charts for males and females        
    bar_one = go.Bar( name = 'Male', x = men_bin, y = age_band[1:], orientation = 'h', text = men_bin, hoverinfo = 'text' )
    bar_two = go.Bar( name = 'Female', x = women_bin, y = age_band[1:], orientation = 'h', text = women_bin, hoverinfo = 'text' )
    
    # add horizontal histograms to figure objects        
    fig.add_trace( bar_one, row = 1, col = 1 )
    fig.add_trace( bar_two, row = 1, col = 2 )
    
    maximum = np.concatenate((women_bin, men_bin)).max()
    
    fig.update_xaxes( autorange = 'reversed', row = 1, col = 1, range = [0, 200000] )
    fig.update_xaxes( autorange = False, row = 1, col = 2, range = [0, maximum] )
    fig.update_xaxes( title_text = 'Number of Accidents', row = 1, col = 1 )
    fig.update_yaxes( title_text = 'Age Band of Driver', row = 1, col = 1 )
    fig.update_yaxes( showticklabels = False, row = 1, col = 2 )
            
    return fig
