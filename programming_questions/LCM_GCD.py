#LCM
def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            result = greater
            break
        greater += 1
    return result


# print(lcm(3, 10))

#GCD
def GCD(a, b):
    hcf = 1
    for i in range(2, a+1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf


# print(GCD(6, 12))

# Using recursion
def GCD_recur(a, b):
    if b == 0:
        return a
    return GCD_recur(b, a % b)


print(GCD_recur(6, 12))
