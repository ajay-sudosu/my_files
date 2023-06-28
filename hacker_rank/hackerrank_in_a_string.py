def check(text):
    default = 'hackerrank'
    last_pos = 0
    for i in default:
        for j in range(last_pos, len(text)):
            if i == text[j]:
                last_pos = j+1
                break
        else:
            return 'NO'
    else:
        return 'YES'


print(check('hereiamstackerrank'))

