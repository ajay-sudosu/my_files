def remove_repeated(s):
    unique = set()
    result = ""
    for i in s:
        if i not in unique:
            unique.add(i)
            result += i
    return result


print(remove_repeated("thisis"))
