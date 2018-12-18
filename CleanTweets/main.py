from load_data import load_data
from preprocessing import remove_pattern, remove_stop_words, drop_col_remove_noneng
from tokenize_and_stem import tokenize_and_stem
from sentiment_analysis import sentiment_analysis

def main():
    tweets_df = load_data()
    tweets_df = remove_pattern(tweets_df)
    tweets_df = remove_stop_words(tweets_df)
    tweets_df = tokenize_and_stem(tweets_df)
    tweets_df = drop_col_remove_noneng(tweets_df)
    tweets_df = sentiment_analysis(tweets_df)
    return tweets_df

if __name__ == '__main__':
    main()
