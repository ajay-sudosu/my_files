n =10
def test(n):
    if n > 0:
        test(n-1)
        print(n)
test(n)