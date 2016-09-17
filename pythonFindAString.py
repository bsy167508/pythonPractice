string, substr = [raw_input() for _ in range(2)]
count=0
for _ in range(len(string)):
	if string[_:len(substr)+_]==substr:
		count+=1
print count