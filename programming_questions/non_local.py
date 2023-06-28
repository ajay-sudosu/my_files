# non local
def outer():
    c = 10

    def inner():
        nonlocal c
        c = 20
    inner()
    print("c is {}".format(c))


outer()