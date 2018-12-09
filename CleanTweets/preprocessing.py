def remove_pattern(df):
    """This function removes the user handle, URL, emoticons, and stop words."""
    df['tidy_tweet'] = df['text'].str.replace(r'@[\w]*', '')
    df['tidy_tweet'] = df['tidy_tweet'].str.replace(r'https?:\/\/.*[\r\n]*', '')
    df['tidy_tweet'] = df['tidy_tweet'].str.replace("[^a-zA-Z#]", " ")
    return df

def remove_stop_words(df):
    df['tidy_tweet'] = df['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
    return df

def drop_col_remove_noneng(df):
    """This function only keeps columns that we need and drops all tweets not in english."""
    df = df.loc[:,['created_at','lang','user_location','text', 'tidy_tweet']]
    df = df[df['lang'].str.contains('en', na = False)]
    return df
