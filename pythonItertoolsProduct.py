from itertools import product
print list(product([1,2,3],[2,3,4]))
print list(product([1,2,3], repeat=2))
print list(product([1,2,3], repeat=3))
print list(product([1,2,3],[3,4]))
A = [[1,2,3],[3,4,5]]
print list(product(*A))
B = [[1,2,3],[3,4,5],[7,8]]
print list(product(*B))

print "Now questions solution"
A = map(int, raw_input().split()) 
B = map(int, raw_input().split())
for i in list(product(A,B)): 
	print i,