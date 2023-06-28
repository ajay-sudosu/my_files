def fibo(n):
    if n <= 0:
        return 0
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n-2):
        a, b = b, a + b
        print(b)


fibo(5)
exit()


# using recursion
def fibo_recur(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibo_recur(n-1) + fibo_recur(n-2)


for i in range(5):
    print(fibo_recur(i))

