from itertools import combinations_with_replacement
print list(combinations_with_replacement('12345',2))
A = [1,1,3,3,3]
print list(combinations(A,2))
a,b = raw_input().split() 
for i in combinations_with_replacement(sorted(a),int(b)):
	print ''.join(i)