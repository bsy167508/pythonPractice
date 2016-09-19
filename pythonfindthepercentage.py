x=int(raw_input().strip())

ls={}

for _ in range(x):
	
	temp = raw_input().split(' ')
	
	ls[temp[0]] = [float(temp[1]), float(temp[2]), float(temp[3])]

name = raw_input()

print ("{0:.2f}".format(sum(ls[name])/3))