def dropcolsremovenoneng(df):
    """This function drops unnecessary columns and any tweets that are not in english."""
    df = df.loc[:,['created_at','lang','user_location','text', 'tidy_tweet']]
    df = df[df['lang'].str.contains('en', na = False)]
    return df
