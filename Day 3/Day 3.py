# Day 3

import math

inp = 368078
# inp = 1024
n = 0
min_dist = 1000000

for c in range(0, 400000):
    sqr = int(math.sqrt(c))
    if sqr % 2 == 1:
        if c == sqr*sqr:
            if abs(inp - c) < min_dist:
                min_dist = abs(inp - c)
                n = sqr

# Probably flawed logic, but it works for my input
print 'Part 1: ' + str(min_dist)
# Part 2 done in excel, rather easily
    