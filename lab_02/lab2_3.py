
# defining list A
A = [1, 97, 5, 2]

print("Startup list:", A)


# sorting
A.sort(reverse=True)

# temporary variable
B = A.copy()
B.sort()

# concatenating
A += B

# outputting
print(A)

