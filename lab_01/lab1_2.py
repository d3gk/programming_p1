
# v - Speed
# s - Distance
# ice - Ice on road (bool)

def b(v, s, ice):
    return (ice and (s <= v + 0.5)) or ((not ice) and (s <= v/2 + 0.5))


print('\n')

# Speed = 20 m/s, Distance = 20 m, no ice, break = false
print('Speed = 20 m/s, Distance = 20 m, no ice, break = false')
print('expected=false')
print(b(20, 20, False))
print('\n')

# Speed = 20 m/s, Distance = 10.5 m, no ice, break = true
print('Speed = 20 m/s, Distance = 10.5 m, no ice, break = true')
print('expected=true')
print(b(20, 10.5, False))
print('\n')

# Speed = 35 m/s, Distance = 10 m, no ice, break = true
print('Speed = 35 m/s, Distance = 10 m, no ice, break = true')
print('expected=true')
print(b(35, 10, False))
print('\n')

# Speed = 20 m/s, Distance = 21 m, ice, break = false
print('Speed = 20 m/s, Distance = 21 m, ice, break = false')
print('expected=false')
print(b(20, 21, True))
print('\n')

# Speed = 20 m/s, Distance = 20.5 m, ice, break = true
print('Speed = 20 m/s, Distance = 20.5 m, ice, break = true')
print('expected=true')
print(b(20, 20.5, True))
print('\n')

# Speed = 20 m/s, Distance = 5 m, ice, break = true
print('Speed = 20 m/s, Distance = 5 m, ice, break = true')
print('expected=true')
print(b(20, 5, True))
print('\nend\n')
