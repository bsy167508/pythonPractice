a = raw_input()
b = raw_input().split(" ")
b = [int(x) for x in b]
setB = set(b)
print sum(setB)/float(len(setB))