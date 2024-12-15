
# defining list

A = [2, 8, 0, -3, 8, -7, 4, 2, 5, -1, 8, 0, 5, -1, 2, 0, 1]

# lopping and calculating the result
i = 0
res = 0
while i < len(A):
    if A[i] < 0:
       res += A[i] 
    i += 1
    
print(res)