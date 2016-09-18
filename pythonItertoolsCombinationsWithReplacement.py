from itertools import combinations_with_replacement
print list(combinations_with_replacement('12345',2))
A = [1,1,3,3,3]
print list(combinations(A,2))
str , n = raw_input().split() 
print("\n".join(x[0]+x[1] for x in combinations_with_replacement (sorted(str),int(n))))