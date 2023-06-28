rows = 5

for i in range(1, 2*rows):
    if i <= rows:
        stars = i
    else:
        stars = 2 * rows - i

    spaces = rows - stars

    print(spaces * "-" + stars * "* ")
