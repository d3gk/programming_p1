
# function
def f(l, k):
    if k >= len(l):
        return None
    l.pop(k)
    return l


# defining list
lst = [1, 2, 3, 4]

print(lst)

# performing action on list lst: f(lst, 8)
lst = f(lst, 8)
print(lst)

# restoring lst's original value
lst = [1, 2, 3, 4]

# performing action on list lst: f(lst, 0)
lst = f(lst, 0)
print(lst)


    