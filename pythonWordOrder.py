from collections import OrderedDict
d = OrderedDict()
for _ in range(int(raw_input())):
    word = raw_input().strip()
    d[word] = d.get(word, 0) + 1
print len(d)
for _ in d.items():
    print _[1],