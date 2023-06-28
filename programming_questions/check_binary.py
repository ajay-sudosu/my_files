def binary(n):
    while n > 0:
        remain = n % 10
        if remain in [1, 0]:
            n = n // 10
        else:
            return "No it is not a binary number"
    else:
        return "Yes it is binary"


print(binary(10101))
