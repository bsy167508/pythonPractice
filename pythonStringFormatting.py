n = int(raw_input())
width = len("{0:b}".format(n)) #equal to len(bin(2)[2:])
print ("{0:{width}b}".format(n,width=3)) #binary
print ("{0:d}".format(n)) #decimal equal to print bin(2)[2:]
print ("{0:x}".format(n)) #hexadecimal equal to print hex(2)[2:]
print ("{0:X}".format(n)) #Hexadecimal Capital equal to print hex(2)[2:].upper()
print ("{0:o}".format(n)) #Octal equal to print oct(2)[2:]
#0 is the index indicating which format argument should be placed in that spot. For example here b means binary and {0:b}
for i in range(1,n+1):
	print "{0:d} {0:o} {0:X} {0:b}".format(i)