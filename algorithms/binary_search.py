# Time complexity
# best = O(1)
# Average = O(log n)

lt=[3,4,5,7,9]
x=90

def search(x):
    l=0
    u=len(lt)-1
    while l<=u:
        mid = (l+u)//2
        if lt[mid] == x:
            return ('found at index {}'.format(mid))
        else:
            if x > lt[mid]:
                l=l+1
            else:
                u=u-1
    else:
        return 'not found'

result= search(x)
print(result)