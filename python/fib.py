#!/usr/bin/env python
import string
import random
import sys
import math
from optparse import OptionParser

""" author: Patrick Kaster (kaster@cs.uni-bonn.de) """


if __name__ == "__main__":

    	desc="""
		%prog [options]\n - %prog: calc. the limit of the Fibonacci sequence, printing the difference to the true solution
	     """
	parser = OptionParser(desc)
    	parser.add_option("-n", dest="n", help="number of iterations", metavar="NUMBER", type="int", default=20)
   	(options, args) = parser.parse_args()
		
	lenN = len(str(options.n))
	cache = [0]*options.n
	cache[0] = 0
	cache[1] = 1

	for i in range (2, options.n):
		cache[i] = cache[i-1] + cache[i-2]
		
	for i in range (2, options.n):
		ratio = float(cache[i])/float(cache[i-1])
		diff = abs(ratio-((1+math.sqrt(5))/2))
		print ("n: {1:{0}d}, ratio: {2:e}, diff: {3:e}".format(lenN, i, ratio, diff))
