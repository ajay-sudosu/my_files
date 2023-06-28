'''
Given a string = 'aabbbccccaa'
output  = 'a2b3c4a2
'''


def string_comp(s):
    a = ''
    count = 1
    for i in range(1, len(s)):
        pre = s[i - 1]
        if pre == s[i]:
            count += 1
        else:
            a = a + s[i - 1] + str(count)
            count = 1
    a = a + s[i] + str(count)
    return a


print(string_comp('aabbbccccaa'))
