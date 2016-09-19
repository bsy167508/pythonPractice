from itertools import combinations

s , n  = raw_input().split()

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print ''.join(j)
print list(combinations('12345',2))
A = [1,1,3,3,3]
print list(combinations(A,4))