#!/usr/bin/env python
import tweepy
api = tweepy.API()
tweet = api.search("beer")[0]
print tweet.text
