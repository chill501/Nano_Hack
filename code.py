#usr/bin

import sys
inFile = sys.argv[1]

with open(inFile,'r') as i:
  for line in i:
    if line.startswith(">") and ("Barcoding_2d" in line):
       print(line)
       print(next(i))
