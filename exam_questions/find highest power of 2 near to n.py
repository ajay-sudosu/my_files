def power (x,y):
    if y==0 :
        return 1
    elif y==1:
        return x
    else:
        return x * power(x,y-1)
n = 10
def test(n):
    if n == 0:
        return 0
    else:
        for i in range(n+1):
            if power(2,i)>n:
                return(i-1)
            elif power(2,i) == n:
                return i

print(test(n))

