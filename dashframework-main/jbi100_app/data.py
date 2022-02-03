import pandas as pd

def get_data():
    # Read data
    df = pd.read_csv('C:/Users/Tychon Bos/Google Drive/CSAI/Visualization/x.csv', sep= ';')
    # Any further data preprocessing can go her
    df['male'] = df['male'].astype(str).astype(int)
    df['female'] = df['female'].astype(str).astype(int)
    df['other'] = df['other'].astype(str).astype(int)
    print(df.columns)
    

get_data()