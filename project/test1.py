import random

gradeMarks = ['a', 'a-','b', 'b-', 'c', 'c-', 'd', 'e', 'f']
list1=[]
for i in [1,2]:
    list1=list1+random.sample(gradeMarks, 8)
print list1