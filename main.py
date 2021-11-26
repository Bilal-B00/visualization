import pandas as pd

data = pd.read_csv('C:/Users/Bilal/Downloads/dataset.csv')

class notAnInteger(Exception):
    pass

class notPandasDataFrame(Exception):
    pass

# parsing function
def parsing(data, row, col):
    try:
        if type(row) != int or type(col) != int:
            raise notAnInteger
        elif type(data) != pd.core.frame.DataFrame:
            raise notPandasDataFrame
        else:
            print(data.loc[row][col])
    except notAnInteger:
        print('One or both of the provided input is not an integer value')
    except notPandasDataFrame:
        print('Dataset provided is not a Pandas DataFrame')
    
    
parsing(data,0,0)