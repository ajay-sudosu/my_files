def count_consecutive_num(s):
    count = 0
    prev_count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1] - 1:
            count += 1
            if count > prev_count:
                prev_count = count
        else:
            count = 0

    return prev_count + 1 if prev_count > 0 or len(s) == 2 and abs(s[0]-s[1] == 1) else 0


# num = [1, 2, 3, 6, 5, 6, 7, 8, 9, 10]
num = [3, 4]
print(count_consecutive_num(num))
