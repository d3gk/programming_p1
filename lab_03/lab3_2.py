
# defining list
list = [2, 8, 0, -3, 8, -7, 4, 2, 5, -1, 8, 0, 5, -1, 2, 0, 1]

# defining counters
less = 0
equal = 0
greater = 0

# counting number of elements, which match criterias
for el in list:
    if el < 2:
        less += 1
    if el > 2:
        greater += 1
    if el == 0:
        equal += 1
    
# outputting
print(f'Less, than 2   :  {less}')
print(f'Equals 0       :  {equal}')
print(f'Greater, than 2:  {greater}')

