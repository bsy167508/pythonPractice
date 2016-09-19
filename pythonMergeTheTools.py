s = raw_input()
k = input()
chunks = len(s)/k

for index in xrange(chunks):
    merge = ""
    T = s[index*k : (index+1)*k]
    for ch in T:
        if ch not in merge:
            merge += ch
    print merge