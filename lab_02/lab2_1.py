
# Declaring string variable, containing float value in text format
stringvar = "12.56"

# Explicitly converting string variable to float, since direct conversion to int is impossible
floatvar = float(stringvar)

# Explicitly converting string variable to float, since direct conversion to int is impossible
# intvar = int(stringvar) will throw an exception, since our string contains text representation of float value
intvar = int(floatvar)

print(f'string:\t{stringvar}')
print(f'float: \t{floatvar}')
print(f'int:   \t{intvar}')



