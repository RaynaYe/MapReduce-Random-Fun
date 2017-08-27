#!/usr/bin/python
import sys,re
posttype=r'(?<=PostTypeId=")\d+(?=")'
accept=r'(?<=AcceptedAnswerId=")\d+(?=")'
OwenerUser=r'(?<=OwnerUserId=")\d+(?=")'
row=r'(?<=row Id=")\d+(?=")'
patternposttype = re.compile(posttype)
patternaccept = re.compile(accept)
patternOwnerUser=re.compile(OwenerUser)
patternrow=re.compile(row)
for line in sys.stdin:
    line=line.strip()
    if re.findall(patternposttype,line)==['1']:
        if re.findall(patternaccept,line)!=[]:
            print ''.join(re.findall(patternaccept,line)),'/t'
    if re.findall(patternposttype,line)==['2']:
        OwnerId=''.join(re.findall(patternOwnerUser,line))
        rowid=''.join(re.findall(patternrow,line))
        print rowid,'/t',OwnerId