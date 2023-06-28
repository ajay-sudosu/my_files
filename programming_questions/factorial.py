# Using recursion method
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


print(fact(5))


# Using iterative method
def fact_(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


print(fact_(5))
