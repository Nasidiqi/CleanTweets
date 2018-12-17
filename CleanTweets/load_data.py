import pandas as pd
import os

def load_data():
    df = pd.read_excel('Data/10.23-10.24.xlsx')
    return df

load_data()
