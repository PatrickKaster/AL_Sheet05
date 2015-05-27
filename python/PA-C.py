#!/usr/bin/env python
import string
import subprocess
from optparse import OptionParser
from tempfile import NamedTemporaryFile
try:
	import matplotlib.pyplot as plt
	PlotAvailable = True
	from time import sleep as sleep
except:
	PlotAvailable = False

""" author: Patrick Kaster (kaster@cs.uni-bonn.de) """


def iterate(system):
	# init livePlot if lib is available	
	if (PlotAvailable):
		plt.figure()
		plt.ion()
		plt.legend()
		plt.show()
	
	i = 1	
	# calc. first predator/prey system	
	if (system==0):
		while (True):
			if( (n>0) & (i==n) ):
				return		
		
			x.append(x[i-1]+a*x[i-1]+b*y[i-1]+e*x[i-1]*x[i-1])
	 		y.append(y[i-1]+c*x[i-1]+d*y[i-1]+f*y[i-1]*y[i-1]) 
		
			if (PlotAvailable):					
				livePlotData()
			i += 1
	# calc. second predator/prey system		
	else:
		while (True):
			if( (n>0) & (i==n) ):
				return		
		
			x.append(x[i-1]+a*x[i-1]+b*y[i-1]+e*x[i-1]*x[i-1]+g*x[i-1]*y[i-1])
	 		y.append(y[i-1]+c*x[i-1]+d*y[i-1]+f*y[i-1]*y[i-1]+h*x[i-1]*y[i-1]) 
		
			if (PlotAvailable):					
				livePlotData()
			i += 1

def livePlotData():
	"""
		plots the calculation "online"
	"""
	prey = plt.plot(range(0, len(x)), x, "GREEN", marker="o", label="prey")
	predator = plt.plot(range(0, len(y)), y, "RED", marker="o", label="predator")
	plt.legend(loc=1, bbox_to_anchor=(0.3, 1))			
	plt.xlabel("time")
	plt.ylabel("population")
	plt.draw()
	plt.clf()
	sleep(SLEEPTIME)


def outputGNUPlot():
	"""
		plots the data via extern GNUPlot call
	"""
	outfileData = NamedTemporaryFile(delete=False)
	# write values of calculation to GNUPlot data file	
	for i in range (0, len(x)):
		outfileData.write("{1:{0}d}, {2:e}, {3:e}\n".format(lenN, i, x[i], y[i]))
	outfileData.close()
	
	# call gnuplot with parameters of plot
	proc = subprocess.Popen(['gnuplot','-p --persist'], shell=False, stdin=subprocess.PIPE) # -persist: python doesn't close GNUPlot window
	proc.stdin.write("set xlabel 'time'; set ylabel 'population'\n;") # label axes
	proc.stdin.write("set label 1 'mean X: {0:e}'; set label 1 at graph 0.02, 0.85 tc lt 3; set label 2 'mean Y: {1:e}'; set label 2 at graph 0.02, 0.80 tc lt 3\n;".format(meanX, meanY)) # print out mean data
	proc.stdin.write("set arrow from {0},0 to {0},100 nohead lc rgb 'red'\n;".format(m)) # mark mean calculation range
	proc.stdin.write("plot '%s' u 1:2 t 'prey' with linespoints lt rgb 'green', '%s' u 1:3 t 'predator' with linespoints lt rgb 'red'\n;" %  (outfileData.name, outfileData.name)) # plot the data for X and Y
	proc.stdin.write("quit\n")

if __name__ == "__main__":

    	desc="""
		%prog [options]\n - %prog: predator/prey system assignment PA-C
	     """
	parser = OptionParser(desc)
    	parser.add_option("-n", dest="n", help="number of iterations", metavar="NUMBER", type="int", default=20)
	parser.add_option("-m", dest="m", help="calc. mean from m till number of iterations", metavar="NUMBER", type="int", default=10)
	parser.add_option("-A", dest="A", help="factor a", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-B", dest="B", help="factor b", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-C", dest="V", help="factor c", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-D", dest="D", help="factor d", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-E", dest="E", help="factor e", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-F", dest="F", help="factor f", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-G", dest="G", help="factor g", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-H", dest="H", help="factor h", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-X", dest="X", help="starting condition for X", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-Y", dest="Y", help="starting condition for Y", metavar="NUMBER", type="float", default=0.1)
	parser.add_option("-T", dest="SLEEPTIME", help="pause between animations steps if plot is rendered", metavar="NUMBER", type="float", default=0.01)
	parser.add_option("-S", "--system", dest="system", help="calc. first(0) or second(1) predator/prey system", metavar="NUMBER", type="int", default=0)
   	(options, args) = parser.parse_args()
	
	# shortcuts	
	n = options.n
	a = options.A
	b = options.B
	c = options.V
	d = options.D
	e = options.E
	f = options.F
	g = options.G
	h = options.H
	m = options.m
	SLEEPTIME = options.SLEEPTIME

	assert m < n

	startingX = options.X
	startingY = options.Y

	x = []
	y = []
	x.append(startingX)
	y.append(startingY)

	# call iteration main loop	
	iterate(options.system)

	lenN = len(str(len(x)))

	# print values of calculation	
	for i in range (0, len(x)):
		print ("n: {1:{0}d}, x: {2:e}, y: {3:e}".format(lenN, i, x[i], y[i]))

	# calc. mean X, Y
	xBar = x[m:]
	yBar = y[m:]

	meanX = sum(xBar)/float(len(xBar))
	meanY = sum(yBar)/float(len(yBar))

	# print mean	
	print ("\nmean x {0:e}, mean y: {1:e}".format(meanX, meanY))

	# output data via GNUPlot	
	outputGNUPlot()
		
