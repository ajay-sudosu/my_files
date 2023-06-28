import numpy as np
a = [[1,2,3],
     [3,4,2],
     [2,3,1]]
b = [[1,2,3],
     [3,4,2],
     [2,3,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j]+=a[i][k]*b[k][j]

for r in result:
    print(r)


# using numpy
# q = np.dot(a,b)
# print(q)


# using list comprehension
result = []


