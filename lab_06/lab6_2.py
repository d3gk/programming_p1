
# function (takes countless amount of parameters, if more, than 2, throws on line 8)
def f(*a):
    if len(a) == 1:
        return a[0] ** 3, None
    if len(a) == 2:
        return a[0] // a[1], a[0] % a[1]
    raise Exception("Wrong input!")

# function demonstration
print(f(32, 12))
print(f(31))
# print(f(1,3,4)) - throws an exception
 
    