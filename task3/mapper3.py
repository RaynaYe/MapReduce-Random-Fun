#!/usr/bin/python
import sys,re
posttype=r'(?<=PostTypeId=")\d+(?=")'
question=r'(?<=ParentId=")\d+(?=")'
OwenerUser=r'(?<=OwnerUserId=")\d+(?=")'
patternposttype = re.compile(posttype)
patternques = re.compile(question)
patternOwnerUser=re.compile(OwenerUser)
for line in sys.stdin:
    if re.findall(patternposttype,line)==['2']:
        quesid=''.join(re.findall(patternques,line))
        OwenerUserid=''.join(re.findall(patternOwnerUser,line))
        print ('{0}^{1}'.format(OwenerUserid, quesid))
