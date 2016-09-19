k,arr = int(raw_input()),list(map(int, raw_input().split()))
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))