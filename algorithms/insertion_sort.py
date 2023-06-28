'''
Start the loop from the first element in the list not the 0th element, store it and also
store 1 less index of current loop index as j(so that we can loop over it).Use while loop to compare all values previous to current value
At last put the stored val into the j+1.
'''

l = [4, 5, 3, 6, 4]

for i in range(1, len(l)):
    val = l[i]    # saving the current value
    j = i-1  # saving just previous index number from the current value so that we can loop through all the previous values to check whether current value is smaller or not
    while j >= 0 and val < l[j]:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = val  # putting value if found smaller to an index number just after which it is compared

print(l)

