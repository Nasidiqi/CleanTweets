def dropcolsremovenoneng(df):
    """This function only keeps columns that we need and drops all tweets not in english."""
    df = df.loc[:,['created_at','lang','user_location','text', 'tidy_tweet']]
    df = df[df['lang'].str.contains('en', na = False)]
    return (df)
