#!/usr/bin/python
import string

class modFile:
    'Modifies a file according to the given problem statement'
    
    def openFile(self, fName):
        'opens the file passed as an argument and enters text in it'
        fo = open(fName, "wb")
        choice='y'
        while choice=='y':
            print "Enter text to be entered in the file:"
            inp = raw_input()
            fo.write(inp+'\n')
            print "Enter more? (y/n)"
            choice=raw_input()
        fo.close()
    
    def modify(self, fName):
        'creates a mod.txt having 2 lines for each corresponding line in orig.txt'
        fo = open(fName, "rb")
        fo2 = open("mod.txt", "wb")
        for line in fo:
            'read the lines from fo and operate upon them'
            line1 = string.capwords(line)
            line2 = ''.join(str(ord(c)) for c in line1)
            fo2.writelines([line1+"\n", line2+'\n'])
        fo.close()
        fo2.close()

'This is our object'
obj = modFile()
obj.openFile("orig.txt")
obj.modify("orig.txt")
print "The contents of the modified file are:"
with open("mod.txt", "rb") as f:
    for line in f:
        print line,
    
        
        