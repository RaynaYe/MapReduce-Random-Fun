#!/usr/bin/python
import sys
prev=0
for line in sys.stdin:
    line=line.strip()
    line=line.split('/t')
    if line[1]:
         owner=line[1]
    if line[0]==prev :
         print owner,prev
    else:
        prev=line[0]
