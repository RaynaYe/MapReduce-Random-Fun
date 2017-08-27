#!/usr/bin/python
import sys
max_list=[]
prev=''
list=[]
owner=''
for line in sys.stdin:
    line=line.strip()
    line=line.split()
    if line[0]==prev:
        list.append(''.join(line[1]))
    else:
        if prev and len(list)>len(max_list):
            max_list=list
            owner=prev
        list=[]
        list.append(''.join(line[1]))
        prev=line[0]
if len(list)>len(max_list):
    max_list=list
    owner=prev
print '\"',owner,'->',(len(max_list)),',',(','.join(max_list[0:])),'\"'