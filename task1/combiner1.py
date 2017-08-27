#!/usr/bin/python
import sys
prev_token=''
prev_txt=''
value_total=1
for line in sys.stdin:
    line=line.strip()
    line,value=line.split('\t',1)
    value=int(value)
    token,txt=line.split('^',1)
    if token == prev_token:
        if txt == prev_txt:
            value_total=value_total+value
        else:
            if prev_token and prev_txt:
                print ('{0}^{1}^{2}'.format(prev_token,prev_txt,value_total))
            prev_txt=txt
            value_total = 1

    else:
        if prev_token and prev_txt:
            print ('{0}^{1}^{2}'.format(prev_token, prev_txt, value_total))
        prev_token=token
        prev_txt=txt
        value_total = 1
if prev_token and prev_txt:
    print ('{0}^{1}^{2}'.format(prev_token, prev_txt, value_total))