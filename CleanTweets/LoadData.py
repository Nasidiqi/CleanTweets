def load_data('data'):
    df= pd.read_excel('data')
    return(df)

def view_head(df):
    x = df.head()
    return(x)
