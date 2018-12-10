# CleanTweets 
Tweet cleaning package

Authors: Jessica Fogerty, Henry Tappa & Krystin Sinclair

This package cleans tweets.

There are five modules in Clean Tweets.

The first is load_data. This module loads one day worth of tweets that have a Bitcoin reference. The day in question is October 23rd. It gets the data from an excel file that is saved inside the data directory  in the cleantweets package folder.

The second module is preprocessing. It contains thre functions. The first removes the user handle, URL,  and emoticons.  The second removes stop words. The third function only keeps the columns that are useful for our needs and it drops all tweets that are not in English. 

The third module is tokenize_and_stem. This function tokenizes the tweets and then stems that back together.

The fourth module is sentiment_analysis. This function performs sentiment analysis on the indiviudal tweets.

The final module is main.py which calls the four modules and runs all function within a main() function.
