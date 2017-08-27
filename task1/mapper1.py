#!/usr/bin/python
import sys,os
for line in sys.stdin:
    line=line.strip()
    for token in line.split():
        path = os.environ["mapreduce_map_input_file"]
        path = path.split('/')
        txt = path[len(path) - 1]
        print ('{0}^{1}^{2}'.format(token, txt, 1))