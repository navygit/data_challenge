# example of program that calculates the median number of unique words per tweet.

import collections

infile = open("tweet_input/tweets.txt")

#returns the number of unique words per tweet
def input():
    for line in infile:
    	    words = collections.Counter()
    	    words.update(line.split())
    	    yield len(words)
    	    
'''
Concept : use a max heap on left side to represent elements that are less than effective median, 
and a min heap on right side to represent elements that are greater than effective median.
After processing an incoming element, the number of elements in heaps differ utmost by 1 element.
When both heaps contain same number of elements, we pick average of heaps root data as effective median.
When the heaps are not balanced, we select effective median from the root of heap containing more elements.
'''    	    
from heapq import heappop, heappush, heappushpop
 
def streaming_median(seq):
    seq = iter(seq)
    left, right  = [], [next(seq)]
    while True:
        yield right[0] if len(right) > len(left) else (right[0] - left[0])/2.0 
        heappush(left, -heappushpop(right, next(seq)))
        if len(left) > len(right):
            heappush(right, -heappop(left))
            
if __name__ == '__main__':
    for x in tuple(streaming_median(input())):
	print x
    
