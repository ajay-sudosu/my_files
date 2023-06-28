l = ["flower", "flow", "floht"]
output_should_be = "flo"


def find_prefix(l):
    min_len = min([len(i) for i in l])
    min_word = [i for i in l if len(i) == min_len][0]
    pre = ''
    done = False
    for i in range(len(min_word)):
        word = min_word[i]
        j = 0
        while j < len(l):
            if l[j][i] == word:
                j += 1
            else:
                done = True
                break
        if done:
            break
        else:
            pre += word
    return pre


print(find_prefix(l))


# 2 method

l = ["flower", "flow", "floht"]


def find_longest_prefix(l):
    if not l:
        return ""

    min_len = min(len(s) for s in l)
    pre = ""

    for i in range(min_len):
        word = l[0][i]
        if all(k[i] == word for k in l):
            pre += word
        else:
            break
    return pre


a = find_longest_prefix(l)
print(a)
