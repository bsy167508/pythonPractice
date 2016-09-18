from collections import deque
d = deque()
d.append(1)
print d
d.appendleft(2)
print d
d.clear()
print d
d.extend('1')
print d
d.extendleft('234')
print d
print d.count('1')
d.pop()
print d
d.popleft()
print d
d.extend('7896')
print d
d.remove('2')
print d
d.reverse()
print d
d.rotate(3)
print d
d = deque()
for _ in range(int(raw_input())):
    inp = raw_input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
for item in d:
    print item,