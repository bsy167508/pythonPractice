#!/bin/python
input = list(raw_input())
temp = raw_input().split(' ')
input[int(temp[0])] = temp[1]
input = "".join(input)
print input