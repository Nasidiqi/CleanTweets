# CleanTweets
Tweet cleaning package

Authors: Jessica Fogerty, Henry Tappa & Krystin Sinclair

This package cleans tweets. 
There are five modules in Clean Tweets. 
The first is LoadData. This module loads one day with of tweets that have a Bitcoin reference. The day in question is October 23rd. It gets the data from an excel file that is saved inside the cleantweets package folder. 
The second module is clean_tweet_remove_pattern. This function removes the user handle, URL, emoticons, and stop words. It also contains a second function which removes stop words. 
The third module is tokenize_and_stem. This function tokenizes the tweets and then stems that back together. 
The fourth module is drop_column_remove_non_english. This function only keeps that columns that are useful for our needs. It also drops all tweets that are not in English. 
The fifth modle is tweet_sentiment. This function performs sentiment analysis on the indiviudal tweets.

The main.py module calls the five modules and runs all function within a __main__ function. 


