'''
*****
 ****
  ***
   **
    *
'''

n =5
space = 0

for i in range(n):
    for i in range(space):
        print(end=' ')
    for j in range(n):
        print('*',end='')
    print()
    n-=1
    space+=1