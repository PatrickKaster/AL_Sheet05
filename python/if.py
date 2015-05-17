#!/usr/bin/env python
import string
import random
import sys
from optparse import OptionParser

""" author: Patrick Kaster (kaster@cs.uni-bonn.de) """

def itFunc(n, a):
	# initialize with startingConditions	
	cache[0]=[0.228734167, 0.228734168]
	
	for i in range (1, n):
		cache[i][0] = float( a * cache[i-1][0] * (1 - cache[i-1][0]) )
		cache[i][1] = float( a * cache[i-1][1] * (1 - cache[i-1][1]) )


if __name__ == "__main__":

    	desc="""
		%prog [options]\n - %prog: calc. iterative function from assignment 36
	     """
	parser = OptionParser(desc)
    	parser.add_option("-n", dest="n", help="number of iterations", metavar="NUMBER", type="int", default=20)
	parser.add_option("-a", dest="a", help="factor a", metavar="NUMBER", type="float", default=3.3)
   	(options, args) = parser.parse_args()
		
	lenN = len(str(options.n))
	cache = [[0]*2]*options.n
	
	itFunc(options.n, options.a)
	
	for i in range (0, options.n):
		print ("n: {1:{0}d}, x_i: {2:e}, xdash_i: {3:e}, diff: {4:e}".format(lenN, i, cache[i][0], cache[i][1], abs(cache[i][0] - cache[i][1])))
