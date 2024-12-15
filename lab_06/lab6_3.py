
# function (expected parameters: l1 - list, l2 - list, oper - string)
def f(l1, l2, oper):
    if not (len(l1) == len(l2)):
        print("Lists must have same length!")
        return None
    if oper == "add":
        lf = []
        for i,j in zip(l1, l2):
            lf.append(i + j)
        return lf
    if oper == "mult":
        lf = []
        for i,j in zip(l1, l2):
            lf.append(i * j)
        return lf
    print("Unexpected operator!")
    return None

# function tests
lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4]
lst3 = [1, 2, 3, 4, 5]

print(f(lst1, lst2, "add"))
print(f(lst1, lst2, "mult"))
print(f(lst1, lst3, "mult"))
print(f(lst1, lst2, "div"))

