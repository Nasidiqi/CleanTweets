import pandas as pd

def load_data():
    df= pd.read_excel('10.23-10.24.xlsx')
    return(df)

load_data()
