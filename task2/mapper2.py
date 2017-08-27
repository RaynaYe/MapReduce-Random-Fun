#!/usr/bin/python
import sys,re
posttype=r'(?<=PostTypeId=")\d+(?=")'
raw=r'(?<=row Id=")\d+(?=")'
viewcount=r'(?<=ViewCount=")\d+(?=")'
patternposttype = re.compile(posttype)
patternraw = re.compile(raw)
patternviewcount=re.compile(viewcount)
for line in sys.stdin:
    if re.findall(patternposttype,line)==['1']:
        rawid=''.join(re.findall(patternraw,line))
        viewcount_number=''.join(re.findall(patternviewcount,line))
        #print ('{0}\t{1}'.format(viewcount_number,rawid))
        print ('{0}\t{1}'.format(viewcount_number, rawid))


