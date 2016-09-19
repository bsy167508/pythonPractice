from collections import defaultdict
d = defaultdict(list)
n,m = map(int,raw_input().strip().split())
[d[raw_input().strip()].append(str(a)) for a in xrange(1,n+1)]
for i in xrange(m):
    f=raw_input().strip()
    if not d[f]:
        print -1
        continue
    print ' '.join(d[f])