
# defining given list
a = [9, 1, 8, 3, 10, 5, 8, 4, 3, 2]

print(a)

# removing minimal and maximal values from list a
a.remove(min(a))
a.remove(max(a))

# creating new list b, based on list a
b = a.copy()

print(b)



