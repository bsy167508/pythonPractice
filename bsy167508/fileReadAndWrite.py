fo = open("sample.txt", "wb")
print "Name of the file "+fo.name

fo.write("This is a text added to the file")
fo.close()


fo = open("sample.txt", "rb")
str = fo.read(10)
print str
fo.close()
