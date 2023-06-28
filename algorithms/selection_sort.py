'''
We will start the loop and then hold the index of current value.Now we will check the index of smallest number
in the list(using another loop) and update index and then just swap the minimum number with the looped number which was in
 continuity in first loop.
 Basically we are comparing number with rest to find smallest and swapping them
'''
l = [4,5,1,6,3]

for i in range(len(l)-1):
    index = i  # saving  the index for lowest value in list
    for j in range(i,len(l)):
        if l[j] < l[index]:
            index = j
    l[i],l[index] = l[index],l[i]


print(l)



