#!/bin/python
i = int(raw_input().strip())
lis = list(map(int,raw_input().strip().split(' ')))
z = max(lis)
while max(lis)==z:
    lis.remove(max(lis))
print max(lis)

