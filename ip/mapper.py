#!/usr/bin/python
import sys

for line in sys.stdin:
	data = line.strip().split("GET ")
	if(len(data) > 1):
		ipname = data[0].split(" ")[0]
		print "{0}\t{1}".format(ipname, 1)

