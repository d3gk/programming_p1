
# defining arrays
arr1 = {5, 7, 9}
arr2 = {9, 7, 10}

# simple function, which checks if an array contains value
def arr_contains(ar, val):
    for v in ar:
        if v == val:
            return True
    return False

# adding one-by-one values, if arr2 does not contain them
for var in arr1:
    if not arr_contains(arr2, var):
        arr2.add(var)


print(arr2)



