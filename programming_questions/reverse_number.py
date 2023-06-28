def rev(n):
    rev_num = 0
    while n > 0:
        remain = n % 10
        n = n // 10
        rev_num = rev_num * 10 + remain
    return rev_num


print(rev(456))
