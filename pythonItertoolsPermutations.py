from itertools import permutations
print permutations(['1','2','3'])
print list(permutations(['1','2','3']))
print list(permutations(['1','2','3'],2))
print list(permutations('abc',3))
a = raw_input().split(" ")

from itertools import permutations

b = list(permutations(a[0], int(a[1])))

for v in sorted(b):
    print("".join(v))