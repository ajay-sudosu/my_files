s = "beautiful"

#  using for loop
def count_vow(s):
    count = 0
    prev_count = 0
    vow = "AEIOUaeiou"
    for i in s:
        if i in vow:
            count += 1
            if count > prev_count:
                prev_count = count
        else:
            count = 0

    return prev_count


# print(count_vow(s))


# using while loop

def count_vow_(s):
    count = 0
    prev_count = 0
    vow = "AEIOUaeiou"
    i = 0
    while i < len(s):
        if s[i] in vow:
            count += 1
            if count > prev_count:
                prev_count = count
            i += 1
        else:
            count = 0
            i += 1
    return prev_count


print(count_vow_(s))
