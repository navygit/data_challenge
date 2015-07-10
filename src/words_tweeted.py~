# example of program that calculates the total number of times each word has been tweeted.

import collections
import operator

infile = open("tweet_input/tweets.txt")
words = collections.Counter()

for line in infile:
    words.update(line.split())    
                                 
for word, count in words.iteritems():
    print word, count
