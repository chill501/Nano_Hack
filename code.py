#!/usr/bin/env python

import sys
inFile = sys.argv[1]
outFile = '2d' + inFile

with open(inFile,'r') as i, open(outFile, 'w') as o:
	for line in i:
		if line.startswith(">") and ("Barcoding_2d" in line):
			o.write(line)
			o.write(next(i))
