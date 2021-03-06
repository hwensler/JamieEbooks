#!/usr/bin/python

#Filename: ebooks.py
from __future__ import print_function

import random
import re
import sys
import twitter
import markov
import time
from htmlentitydefs import name2codepoint as n2c
from local_settings import *

#open output logs
f = open(LOGS,'a')

#record start time
current_time = time.strftime("%m.%d.%y %H:%M", time.localtime())
print(current_time, file = f)

def connect():
    api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
                          consumer_secret=MY_CONSUMER_SECRET,
                          access_token_key=MY_ACCESS_TOKEN_KEY,
                          access_token_secret=MY_ACCESS_TOKEN_SECRET)
    return api

def entity(text):
    if text[:2] == "&#":
        try:
            if text[:3] == "&#x":
                return unichr(int(text[3:-1], 16))
            else:
                return unichr(int(text[2:-1]))
        except ValueError:
            pass
    else:
        guess = text[1:-1]
        numero = n2c[guess]
        try:
            text = unichr(numero)
        except KeyError:
            pass    
    return text

def filter_tweet(tweet):
    tweet.text = re.sub(r'\b(RT|MT) .+','',tweet.text) #take out anything after RT or MT
    tweet.text = re.sub(r'(\#|@|(h\/t)|(http))\S+','',tweet.text) #Take out URLs, hashtags, hts, etc.
    tweet.text = re.sub(r'\n','', tweet.text) #take out new lines.
    tweet.text = re.sub(r'\"|\(|\)', '', tweet.text) #take out quotes.
    htmlsents = re.findall(r'&\w+;', tweet.text)
    if len(htmlsents) > 0 :
        for item in htmlsents:
            tweet.text = re.sub(item, entity(item), tweet.text)    
    tweet.text = re.sub(r'\xe9', 'e', tweet.text) #take out accented e
    return tweet.text
                     
                     
                                                    
def grab_tweets(api, max_id=None):
    source_tweets=[]
    user_tweets = api.GetUserTimeline(screen_name=user, count=3200, max_id=max_id, include_rts=True, trim_user=True, exclude_replies=True)
    max_id = user_tweets[len(user_tweets)-1].id-1
    for tweet in user_tweets:
        tweet.text = filter_tweet(tweet)
        if len(tweet.text) != 0:
            source_tweets.append(tweet.text)
    return source_tweets, max_id

if __name__=="__main__":
    order = ORDER
    if DEBUG==False:
        guess = random.choice(range(ODDS))
    else:
        guess = 0

    if guess == 0:
        if STATIC_TEST==True:
            file = TEST_SOURCE
            print(">>> Generating from {0}".format(file), file = f)
            string_list = open(file).readlines()
            for item in string_list:
                source_tweets = item.split(",")    
        else:
            source_tweets = []
            for handle in SOURCE_ACCOUNTS:
                user=handle
                api=connect()
                try:
                    handle_stats = api.GetUser(screen_name=user)
                except:
                    print("!!!PROBLEM WITH USER!!!", file = f)
                    handle_stats = None
                if handle_stats is not None:
                    status_count = handle_stats.statuses_count
                    max_id=None
                    if status_count<3200:
                        my_range = (status_count/200) + 1
                    else:
                        my_range = 17
                    for x in range(my_range)[1:]:
                        source_tweets_iter, max_id = grab_tweets(api,max_id)
                        source_tweets += source_tweets_iter
                    print("{0} tweets found in {1}".format(len(source_tweets), handle), file = f)
                    if len(source_tweets) == 0:
                        print("Error fetching tweets from Twitter. Aborting.", file = f)
                        sys.exit()
        mine = markov.MarkovChainer(order)
        for tweet in source_tweets:
            if re.search('([\.\!\?\"\']$)', tweet):
                pass
            else:
                tweet+="."
            mine.add_text(tweet)
            
        for x in range(0,10):
            ebook_tweet = mine.generate_sentence()

        #randomly drop the last word
        if random.randint(0,4) == 0 and re.search(r'(in|to|from|for|with|by|our|of|your|around|under|beyond)\s\w+$', ebook_tweet) != None: 
           print("Losing last word randomly", file = f)
           ebook_tweet = re.sub(r'\s\w+.$','',ebook_tweet) 
           print (ebook_tweet, file = f)
    
        #if a tweet is short, add another sentence
        if ebook_tweet != None and len(ebook_tweet) < 40:
            rando = random.randint(0,10)
            if rando == 0 or rando == 7: 
                print("Short tweet. Adding another sentence randomly", file = f)
                newer_tweet = mine.generate_sentence()
                if newer_tweet != None:
                    ebook_tweet += " " + mine.generate_sentence()
                else:
                    ebook_tweet = ebook_tweet
            elif rando == 1:
                #make a thing ALL CAPS
                print("ALL CAPS ADDED", file = f)
                ebook_tweet = ebook_tweet.upper()

        #throw out tweets that match anything from the sources
        if ebook_tweet != None and len(ebook_tweet) < 110:
            for tweet in source_tweets:
                if ebook_tweet[:-1] not in tweet:
                    continue
                else: 
                    print("TOO SIMILAR: " + ebook_tweet, file = f)
                    sys.exit()
                          
            if DEBUG == False:
                status = api.PostUpdate(ebook_tweet)
                print(status.text.encode('utf-8'), file = f)
            else:
                print(ebook_tweet, file = f)

        elif ebook_tweet == None:
            print("Tweet is empty, sorry.", file = f)
        else:
            print("TOO LONG: " + ebook_tweet, file = f)
    else:
        print(str(guess) + " No, sorry, not this time." , file = f) #message if the random number fails.