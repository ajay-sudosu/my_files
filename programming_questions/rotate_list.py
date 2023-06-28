# rotate left
def rotate_left(l, r):
    for i in range(r):
        last_val = l[-1]
        for j in range(len(l)-1, -1, -1):
            l[j] = l[j-1]
        l[0] = last_val

    return l


print(rotate_left([3, 4, 5, 8, 1], 2))


# rotate right
def rotate_right(l, r):
    for i in range(r):
        first_value = l[0]
        for j in range(len(l)-1):
            l[j] = l[j+1]
        l[-1] = first_value

    return l


print(rotate_right([3, 4, 5, 8, 1], 2))
