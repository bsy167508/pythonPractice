n, m = map(int, raw_input().split())
arr = [int(x) for x in raw_input().split()]
A = set([int(y) for y in raw_input().split()])
B = set([int(z) for z in raw_input().split()])
count = [1 if x in A else 0 -1 if x in B else 0 for x in arr]
print(sum(count))