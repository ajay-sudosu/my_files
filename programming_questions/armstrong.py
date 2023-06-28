def order(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


def power(x, y):
    if y == 1:
        return x
    elif y == 0:
        return 1
    return x * power(x, y-1)


def check_armstrong(n):
    o = order(n)
    temp = n
    arm_strong = 0
    while temp > 0:
        remain = temp % 10
        temp = temp // 10
        arm_strong = arm_strong + power(remain, o)
    if n == arm_strong:
        return f"Yes it is an armstrong number."
    return "No it is not"


print(check_armstrong(153))
