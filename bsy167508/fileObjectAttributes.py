fo = open("sample.txt", "wb")
print "Name of the file "+fo.name
print "Closed or not:", fo.closed
print "File opening mode", fo.mode
print "Softspace flag", fo.softspace
fo.close()

