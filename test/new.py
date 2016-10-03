import random, itertools

lis=[]
for i in xrange(4):
    lis = lis+random.sample([k for k in xrange(3,11)],8)

lis2 = list(enumerate(lis))
for i in xrange(32):
    lis2[i]=tuple(reversed(lis2[i]))