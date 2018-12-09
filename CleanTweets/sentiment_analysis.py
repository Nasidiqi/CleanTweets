from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger

def sentiment_analysis(df):
    """This function performs the sentiment analysis and returns the polarity
    and subjectivity of the tweet."""
    df['sentiment'] = df['tidy_tweet'].apply(lambda tweet: TextBlob(tweet).sentiment)
    return df
