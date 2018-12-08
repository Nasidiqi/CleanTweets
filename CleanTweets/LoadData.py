import pandas as pd

def load_data(df='10.23-10.24/xlsx'):
    df= pd.read_excel(df)
    return(df)
load_data()
