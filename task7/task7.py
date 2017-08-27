import sys
from bitarray import bitarray
import mmh3

param = int(sys.argv[1])
size = param * 10  # set the bitarray size
hash_count = 7
bit_array = bitarray(size)
bit_array.setall(0)

for line in sys.stdin:
    line = line.strip()
    line_in = True
    for seed in xrange(hash_count):
        result = mmh3.hash(line, seed) % size
        if bit_array[result] == 0:
            line_in = False
            bit_array[result] = 1
    if line_in == False:
        print line


