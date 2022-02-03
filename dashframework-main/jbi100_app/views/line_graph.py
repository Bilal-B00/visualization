import plotly.express as px
import pandas as pd
import numpy as np

def linegraph(accident_index, year_col, sex_of_driver, sex_col ,df): #intialize function with parameters to create linegraph
    
    genders = {} 
    for sex in sex_of_driver: #loop through genders
        genders[str(sex)] = []


    year = np.sort(df[year_col].unique()) #sort year

    for i in year: # loop through year
        for key in genders: #loop through genders
            if int(key) == 4: #assign values: 1 male, 2 female, 3 other, 4 total
                genders[key].append(df[df[year_col] == i][accident_index].unique().shape[0]) #count total accidents for each year
            else:
                genders[key].append( df[ (df[year_col] == i) & (df[sex_col] == int(key)) ][accident_index].unique().shape[0]) #count total accidents for male, female or other
      
    d = {}
    d['year' ] = year    
    for key in genders: #loop through genders and value for genders
        if int(key) == 1:
            d['male'] = genders[key]
        elif int(key) == 2:
            d['female'] = genders[key]
        elif int(key) == 3:
            d['other'] = genders[key]
        else:
            d['total'] = genders[key]
        
    df1 = pd.DataFrame(data=d)  
    df1.set_index('year')
    fig = px.line(df1, x='year', y=df1.columns[0:len(sex_of_driver)+1], title='Amount of accidents for each year (2016-2020)') #make linegraph
    fig.update_xaxes(type='category') 
    return fig
