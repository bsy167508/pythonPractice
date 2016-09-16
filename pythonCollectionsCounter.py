#!/bin/python

from collections import Counter

noOfShoes=int(raw_input().strip())
shoeSizes=Counter(map(int,raw_input().strip().split(' ')))
noOfCustomers=int(raw_input().strip())
total=[]
for i in range(noOfCustomers):
	a,b = map(int, raw_input().strip().split(' '))
	if shoeSizes[a]>0:
		total.append(b)
		shoeSizes.subtract(Counter([a]))
print sum(total)
