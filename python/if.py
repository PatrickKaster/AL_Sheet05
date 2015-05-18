#!/usr/bin/env python
import string
import random
import sys
from optparse import OptionParser

""" author: Patrick Kaster (kaster@cs.uni-bonn.de) """


if __name__ == "__main__":

    	desc="""
		%prog [options]\n - %prog: calc. iterative function from assignment 36
	     """
	parser = OptionParser(desc)
    	parser.add_option("-n", dest="n", help="number of iterations", metavar="NUMBER", type="int", default=20)
	parser.add_option("-a", dest="a", help="factor a", metavar="NUMBER", type="float", default=3.3)
   	(options, args) = parser.parse_args()
		
	lenN = len(str(options.n))
	
	n = options.n
	a = options.a
	
	cache = [[0]*2]*n
	cache[0] = [0.228734167, 0.228734168]

	for i in range (1, n):
		cache[i] = [ a*cache[i-1][0]*(1-cache[i-1][0]), a*cache[i-1][1]*(1-cache[i-1][1]) ]		
		

	for i in range (0, n):
		diff = abs( cache[i][0] -  cache[i][1] )		
		print ("n: {1:{0}d}, x_i: {2:e}, xdash_i: {3:e}, diff: {4:e}".format(lenN, i, cache[i][0], cache[i][1], diff))
