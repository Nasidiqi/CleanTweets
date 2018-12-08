import pandas as pd

def load_data():
    df= pd.read_excel('https://sfm.library.gwu.edu/ui/exports/755/file/14a72258a1b441a8a89385a6c1a064ad_001.xlsx')
    return(df)
load_data()

df.head()
