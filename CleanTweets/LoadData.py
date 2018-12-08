import pandas as pd

<<<<<<< HEAD
def load_data(df='10.23-10.24/xlsx'):
    df= pd.read_excel(df)
    return(df)
load_data()
=======
def load_data(df):
    df = pd.read_excel('10.23-10.24.xlsx')
    return(df)

load_data(df)
>>>>>>> ffc8c1f7c632d4a1330446926c9a517b06049241
