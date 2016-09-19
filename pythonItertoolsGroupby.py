from itertools import groupby

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
f= lambda x: x[0]
print f([1,2,3])
for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print "A %s is a %s." % (thing[1], key)
    print " "
	
#In this example, things is a list of tuples where the first item in each tuple is the group the second item belongs to.

#The groupby() function takes two arguments: (1) the data to group and (2) the function to group it with.

#Here, lambda x: x[0] tells groupby() to use the first item in each tuple as the grouping key.

#In the above for statement, groupby returns three (key, group iterator) pairs - once for each unique key. You can use the returned iterator to iterate over each individual item in that group.
s = raw_input()
#groupby may fail on lists without key but simple strings it can manage perhaps with a single argument
#here groupby automatically creates a pair key, group with keys being the numbers consecutively repeated and group 
#being the group of each consecutive repetition
#when we print len(list(group)), int(key) we simply print no of repetitions and the number repeated
for key,group in groupby(s):
	print (len(list(group)),int(key)),