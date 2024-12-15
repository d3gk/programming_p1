
# defining starting variables
A = [1, 97, 5, 2, 6, 19, 4, 7, 37, 14, 91, 88, 87]
B = []

# adding each value of list A to list, formatting the values
for num in A:
    B.append(f"{num ** 2} м2")

# outputting all data to the terminal
print("List A:", A)
print("List B:", B)