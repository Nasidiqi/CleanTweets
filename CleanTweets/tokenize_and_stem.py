def tokenizeandstem(df):
    """This function tokenizes the tweets and stems them and then joins them back together."""
    tokenized_tweet = df['tidy_tweet'].apply(lambda x: x.split())
    print('*****')
    stemmer = PorterStemmer()
    tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x])
    for i in range(len(tokenized_tweet)):
        tokenized_tweet[i] = ' '.join(tokenized_tweet[i])
    print('*****')
    df['tidy_tweet'] = tokenized_tweet
    return df
