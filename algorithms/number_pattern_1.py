'''
1
12
123
1234
12345

'''



n = 5
for i in range(1,n+1):
    # space = n-1
    for k in range(1,i+1):
        print(k,end='')
    for j in range(n):
        print(end=' ')


    print()
    n-=1

#   Next Pattern

#
#      1
#     12
#    123
#   1234
#  12345
#
# n = 5
# for i in range(1,n+1):
#     # space = n-1
#
#     for j in range(n):
#         print(end=' ')
#     for k in range(1,i+1):
#         print(k,end='')


    print()
    n-=1