#!/usr/bin/python
import sys

totalHit = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
	
    if len(data_mapped) != 2:        
	continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
	print oldKey, "\t", totalHit
	oldKey = thisKey
	totalHit = 0

    oldKey = thisKey
    totalHit += int(thisHit)

if oldKey != None:
    print oldKey, "\t", totalHit 

