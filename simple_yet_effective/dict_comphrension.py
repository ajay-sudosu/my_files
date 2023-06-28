# count the number of words in a string
s = "ajay"
l = list(s)
print(l)
a = {i: sum([1 for j in l if j == i]) for i in l}
print("This is a dict comprehension: ", a)


# list slicing
li = [10, 15, 20, 25]
li[1:3] = [30]
print(li)


# index(index of the first occurrence of the element, start index, end index)
tpl = (1, 2, 3, 3, 4, 5)
print(tpl.index(__value=3, __start=2, __stop=4))
