def power(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    return x * power(x,y-1)


def order(n):
    count = 0
    while n>0:
        count+=1
        n=n//10
    return count


def arm(n):
    number = n
    o = order(n)
    num = 0
    while n>0:
        rem = n%10
        num = num+power(rem,o)
        n = n//10
    if num == number:
        return True
    return False



n = 23
result = arm(n)
print(result)