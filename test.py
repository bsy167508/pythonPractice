from itertools import groupby
s = raw_input()
#groupby may fail on lists without key but simple strings it can manage perhaps with a single argument
#here groupby automatically creates a pair key, group with keys being the numbers consecutively repeated and group 
#being the group of each consecutive repetition
#when we print len(list(group)), int(key) we simply print no of repetitions and the number repeated
for key,group in groupby(s):
	print (len(list(group)),int(key))