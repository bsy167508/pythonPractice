#pythonprint.py
#!/bin/python
from __future__ import print_function

print(*range(1,int(raw_input())+1),sep='')
print "Another Solution"
print "".join([str(i) for i in range(1,int(raw_input())+1)])