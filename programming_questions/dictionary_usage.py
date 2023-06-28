a = "Hihello"
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

# find the key corresponding to the maximum value
k = max(d, key=d.get)
print(k)

# find both the key and value corresponding to the maximum value
result = max(d.items(), key=lambda x: x[1])
# print(result)