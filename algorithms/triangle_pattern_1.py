'''
    *
   **
  ***
 ****
*****
'''
n=5

for i in range(1,n+1):
    space = n-1
    for j in range(space):
        print(end=' ')
    n-=1
    print('*'*i)
