from __future__ import print_function

def rc(r, c):
    rr = r + c - 1
    return 1 - r + (rr * (rr + 1)) // 2

"""
k = 9
for i in range(1, k):
    for j in range(1, k - i):
        print(i, j, rc(i, j))
"""

r, c = 2978, 3083

x = 20151125
for i in range(1, rc(r, c)):
    x = (x * 252533) % 33554393
