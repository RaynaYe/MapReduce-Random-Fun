#!/usr/bin/python
import sys
i=0
for line in sys.stdin:
    line=line.strip()
    viewcount,rawid=line.split('/t',1)
    if i<10:
        print viewcount,rawid
    i=i+1