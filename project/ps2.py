#!usr/bin/python
import string, random, collections

class Parity():
    'class for adding parity bit to the input source bit stream'
    bitStream = '00000000'
    
    def NOT(self, a):
        'returns NOT of the passed bit'
        return 1-a
    
    def XNOR(self, a, b):
        'returns XNOR of the passed bits'
        return self.NOT(a ^ b)
    
    def checkParity(self):
        'checks if even parity or odd parity'
        check = 0
        for bit in self.bitStream:
            check = self.XNOR(check , int(bit))
        if check==1:
            return 'odd'
        else:
            return 'even'
        
        
    def setParity(self, parity):
        'append parity bit in odd parity case'
        if parity=='odd':
            self.bitStream=self.bitStream+'1'
        else:
            self.bitStream=self.bitStream+'0'
    
    def __init__(self, stream):
        self.bitStream = stream
        parity = self.checkParity()
        self.setParity(parity)
    
    def getParity(self):
        parity = self.checkParity()
        self.setParity(parity)
        return self.bitStream

class MatrixCipher():
    'class for encryption using a matrix cipher'
    bitStream = '00000000'
    matrix=[]
    output = ''
    
    def __init__(self, stream):
        self.bitStream = stream
        self.matrix = [string.ascii_uppercase[::-1] if i%2==0 else string.ascii_uppercase for i in range(26)]
    
    def setMatCipher(self):
        for bit in self.bitStream:
            if bit=='1':
               self.output=self.output+self.matrix[random.randint(0,25)]
            else:
                index = random.randint(0,25)
                for line in self.matrix:
                    self.output=self.output+line[index]
    
    def getMatCipher(self):
        self.setMatCipher()
        return self.output
    

class Rotate():
    'rotates the input bit stream randomly'
    bitStream = '00000000'
    def __init__(self, stream):
        self.bitStream = stream
        
    def setRotate(self):
        d = collections.deque([bit for bit in self.bitStream])
        d.rotate(random.randint(0,5))
        return d
    
    def getRotate(self):
        d = self.setRotate()
        return ''.join([bit for bit in d])
    
class Encrypter(Parity, MatrixCipher, Rotate):
    'Class to implement the inherited classes'
    def __init__(self, stream):
        Parity.__init__(self, stream)
        MatrixCipher.__init__(self, stream)
        Rotate.__init__(self, stream)
    
        
while(1):
    print "Enter the input bit stream"
    stream = raw_input()
    obj = Encrypter(stream)
    print "Choose your method of encryption:\n 1- Odd Parity Checking \n 2- Matrix Cipher \n 3- Rotate bit stream randomly \n 4- Break"
    choice = int( raw_input().strip() )
    if choice==1:
        print obj.getParity()
    elif choice==2:
        print obj.getMatCipher()
    elif choice==3:
        print obj.getRotate()
    elif choice==4:
        break
    else:
        print "Enter Again"
    