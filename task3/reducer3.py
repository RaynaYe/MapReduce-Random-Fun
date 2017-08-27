#!/usr/bin/python
import sys
max=0
list_max=[]
for line in sys.stdin:
    print line
    line=line.strip()
    ownerid,quesid=line.split('^',1)
    quesid=quesid.split()
    print quesid
    if len(list_max)<len(quesid):
            list_max=quesid
            max=ownerid
list_max = list(set(list_max))
print max,'->',','.join(list_max)

