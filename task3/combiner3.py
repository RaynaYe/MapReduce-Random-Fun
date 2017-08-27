#!/usr/bin/python
import sys
prev=''
list=[]
for line in sys.stdin:
    line=line.strip()
    ownerid, quesid = line.split('^', 1)
    if ownerid == prev:
        list.append(quesid)
    else:
        if prev:
            print (('{0}^{1}'.format(prev,' '.join(list))))
        list=[]
        list.append(quesid)
        prev=ownerid
if prev:
    print (('{0}^{1}'.format(prev, ' '.join(list))))