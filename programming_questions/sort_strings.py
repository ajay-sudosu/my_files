def sort_string(s):
    result = ""
    for i in range(ord("a"), ord("z")+1):
        for j in s:
            if i == ord(j):
                result += j
    return result


print(sort_string("aales"))
