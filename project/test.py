import heapq, collections

lis = raw_input().split(" ")
newLis = collections.Counter(lis).values()
li=list(enumerate(newLis))
print li
words = collections.Counter(lis).items()
seq = heapq.nlargest(3, newLis)
for s in seq:
    for i in [index for index, value in enumerate(newLis) if value==s]:
            print words[i][0]