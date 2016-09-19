raw_input()
setM = set(map(int, raw_input().split()))
raw_input()
setN = set(map(int, raw_input().split()))
setO = setM.difference(setN).union(setN.difference(setM))
for i in sorted( list( setO )):
	print i
	
print "Another solution"
input()
a=set(map(int,raw_input().split()))
input()
b=set(map(int,raw_input().split()))
c=a.symmetric_difference(b)
for n in sorted(list(c)):
    print n