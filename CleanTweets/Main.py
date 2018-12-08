from LoadData import load_data
from CleanTweetremovePATT import clean_tweet_removepattern, remove_stop_words
from tokenize_and_stem import tokenizeandstem
from drop_column_remove_non_english import dropcolsremovenoneng
from tweet_sentiment import tweet_sentiment

def main():
    tweets_df = load_data()
    tweets_df = clean_tweet_removepattern(tweets_df)
    tweets_df = remove_stop_words(tweets_df)
    tweets_df = tokenizeandstem(tweets_df)
    tweets_df = dropcolsremovenoneng(tweets_df)
    tweets_df = tweet_sentiment(tweets_df)

if __name__ == '__main__':
    main()
main()
