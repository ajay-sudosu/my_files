arr = [10,2,3,4,5,6,7,8,9,10,0]
l = len(arr)
missing =None
for i in range(l):
    if i not in arr:
        missing = i
d = {}
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
key = None
for i,j in d.items():
    if d[i]>1:
        key = i
print(key+missing)