# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:31:05 2022

@author: Bilal
"""

import numpy as np
import pandas as pd
import plotly.express as px

# initialize histogram function
def histogram(col_name, select_col, select_val, x_name, df):
    # calculate histogram without ant=y filtering criteria 
    if select_col == '':
        uniq_x = np.sort(df[(df[col_name] > 0) & (df[col_name] < 24)][col_name].unique())
        freq = []
        for i in uniq_x:
            freq.append(df[df[col_name] == i].shape[0])
        fig = px.bar(x = uniq_x, y = freq)
        fig.update_layout(bargap = 0.2)
        fig.update_xaxes(title_text = "Age Band")
        fig.update_yaxes(title_text = "Number of Accidents")
        return fig
    # calculate histogram with filtering criteria
    else:
        uniq_x = np.sort(df[(df[col_name] > 0) & (df[col_name] < 24)][col_name].unique())
        freq = []
        for i in uniq_x:
            freq.append(df[(df[col_name] == i) & (df[select_col] == select_val)].shape[0])
        fig = px.bar(x = uniq_x, y = freq)
        fig.update_layout(bargap = 0.2)
        fig.update_xaxes(title_text = x_name)
        fig.update_yaxes(title_text = "Number of Accidents")
        return fig