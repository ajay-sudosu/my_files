n = 5
start = 1
for i in range(1,n+1):
    for k in range(start):
        print(start,end='')
        space = n-1
        for j in range(space):
            print(end='-')
    start+=1
    print()