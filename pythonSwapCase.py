print ''.join([i.lower() if i.isupper() else i.upper() for i in raw_input()])
print "Another solution"
print "".join( map (str.swapcase, raw_input() ) )
print "Another solution"
print raw_input().swapcase()