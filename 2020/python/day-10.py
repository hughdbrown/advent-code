from functools import reduce
import re
from pprint import pprint
from collections import deque, Counter
from itertools import accumulate
from heapq import heappush, heappop, heapify

import requests

#url = "https://adventofcode.com/2020/day/4/input"
#r = requests.get(url)
#data = r.text

data = """153
69
163
123
89
4
135
9
124
74
141
132
75
3
18
134
84
15
61
91
90
98
99
51
131
166
127
77
106
50
22
70
43
28
41
160
44
117
66
60
76
17
138
105
97
161
116
49
104
169
71
100
16
54
168
42
57
103
1
32
110
48
12
143
112
82
25
81
148
133
144
118
80
63
156
88
47
115
36
2
94
128
35
62
109
29
40
19
37
122
142
167
7
147
121
159
87
83
111
162
150
8
149"""


def puzzle1(data):
    chain = [0] + sorted((int(d) for d in data.splitlines()))
    print(chain)
    d = Counter()
    for i in range(len(chain) - 1):
        x = chain[i + 1] - chain[i]
        d[x] += 1
    d[3] += 1
    print(d)
    print(d[1] * d[3])


def puzzle2(data):
    chain = [0] + sorted((int(d) for d in data.splitlines()))
    chain.append(chain[-1] + 3)
    x = [0] * (chain[-1] + 1)
    x[0] = 1
    for i in chain[1:]:
        indexes = {max(0, i - j) for j in (1, 2, 3)}
        x[i] = sum(x[j] for j in indexes)
    print(x[-1])


if __name__ == '__main__':
    puzzle1(data)
    puzzle2(data)
