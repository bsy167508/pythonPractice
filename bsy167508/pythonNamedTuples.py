from collections import namedtuple
Point = namedtuple('Point','x, y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print dot_product
Car = namedtuple('Car','Price,Mileage ,Colour ,Class')
#xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
xyz = Car(100000 ,30 ,'Cyan', 'Y')
print xyz
print xyz.Class
from collections import namedtuple
n, Student = int(raw_input().strip()), namedtuple('Student', raw_input())
print "{0:.2f}".format( sum([float(stud.MARKS) for stud in [Student(*raw_input().split()) for _ in xrange(n)]]) / n )