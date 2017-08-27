#!/usr/bin/python
import sys
prev=0
list=[]
for line in sys.stdin:
    line=line.strip()
    line=line.split()
    print ('{0}\t{1}'.format(line[0],line[1]))