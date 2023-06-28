def check_pallindrom(n):
    rev_num = 0
    temp = n
    while temp > 0:
        remain = temp % 10
        temp = temp // 10
        rev_num = (rev_num * 10) + remain
    print(rev_num)
    print(n)
    if rev_num == n:
        return f"Number is {n} and rev_num is {rev_num}, so yes it is an armstrong number"
    else:
        return f"Number is {n} and rev_num is {rev_num}, so no it is not an armstrong number"


# print(check_pallindrom(1531))

# using recursion


