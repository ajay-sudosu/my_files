s = "xxyyxxxzz"


def rem_dup(s):
    result = ''
    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1]:
            result += s[i]

    return result


print(rem_dup(s))
