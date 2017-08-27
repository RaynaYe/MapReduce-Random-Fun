#!/usr/bin/python
import sys
prev_token=''
prev_txt=''
value_total=0
list=[]
for line in sys.stdin:
    token,txt,value=line.strip().split('^',2)
    value=int(value)
    if token==prev_token:
        list.append((txt,value))
        value_total=value_total+1
    else:
        if prev_token:
            print (prev_token,value_total,list)
        list = []
        list.append((txt,value))
        value_total=1
        prev_token=token
if prev_token:
    print (prev_token, value_total, list)


