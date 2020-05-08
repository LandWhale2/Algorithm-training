import sys
from collections import deque

for _ in range(int(input())):
    l = deque()
    r = deque()
    for c in input():
        if c == '<':
            if l:
                r.appendleft(l.pop())
        elif c == '>':
            if r:
                l.append(r.popleft())
        elif c == '-':
            if l:
                l.pop()
        else:
            l.append(c)
    l.extend(r)
    print(''.join(l))