#!/usr/bin/env python
import sys
import random
total=0
for line in sys.stdin:
    line=line.strip()
    number,line=line.split('^',1)
    number=int(number)
    total=total+number
    if random.randint(0,total-1)<number:
        resevoir = line
print resevoir