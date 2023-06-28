# To check if a number is prime or not.
def prime(n):
    if n == 1:
        return "It is not a prime number."
    for i in range(2, n // 2 + 1):
        for j in range(1, i):
            if i % j == 0:
                return "It is not a prime number."
    else:
        return "Yes it is a prime number."


# print(prime(2))


# To check if the number is prime or not in a given range.
def prime_(start, end):
    for i in range(start, end+1):
        if i > 1:
            for j in range(2, i//2+1):
                if i % j == 0:
                    break
            else:
                print(i)


prime_(2, 10)

