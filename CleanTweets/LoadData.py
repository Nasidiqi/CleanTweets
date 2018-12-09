import pandas as pd
import os

def load_data():
    os.chdir('Data')
    df = pd.read_excel('10.23-10.24.xlsx')
    return df
    os.chdir('..')
