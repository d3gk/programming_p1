
# defining list
A = [2, 8, 0, -3, 8, -7, 4, 2, 5, -1, 8, 0, 5, -1, 2, 0, 1]

# defining indexes
i = 0
j = 0 

while i < len(A):
    while j < len(A):
        if (A[i] + A[j]) > 8:
            # outputting formated string with indexes, only if sum of elements is more, than 8
            print(f'{i},\t{j}\t - сума {A[i] + A[j]}')
        j += 1
    i += 1