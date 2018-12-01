def load_data('data'):
    Df= pd.read_excel('data')
    return(Df)

def view_head(Df):
    x = Df.head()
    return(x)
