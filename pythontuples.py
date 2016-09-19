#!/bin/python

x=raw_input().strip()
l=raw_input().strip().split(' ')
#l= map(int, l)
l= [int(x) for x in l]
t=tuple(l)
print hash(t)
