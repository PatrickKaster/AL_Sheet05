#!/usr/bin/env python
import string
import random
import sys
import math
from optparse import OptionParser

""" author: Patrick Kaster (kaster@cs.uni-bonn.de) """

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1

	return float(fib(n-1) + fib(n-2))


if __name__ == "__main__":

    	desc="""
		%prog [options]\n - %prog: calc. the limit of the Fibonacci sequence, printing the difference to the true solution
	     """
	parser = OptionParser(desc)
    	parser.add_option("-n", dest="n", help="number of iterations", metavar="NUMBER", type="int", default=20)
   	(options, args) = parser.parse_args()
		
	lenN = len(str(options.n))
	
	for i in range (2, options.n):
		quotient = fib(i)/fib(i-1)
		diff = abs(quotient-((1+math.sqrt(5))/2));
		print ("n: {1:{0}d}, quotient: {2:e}, diff: {3:e}".format(lenN, i, quotient, diff))
