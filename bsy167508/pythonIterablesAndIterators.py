from itertools import combinations

N = int(raw_input())
L = raw_input().split()
K = int(raw_input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print("{0:.3f}".format(len(list(F))/float(len(C))))