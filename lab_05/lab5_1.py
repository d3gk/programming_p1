
# defining given list
a = [9, 1, 8, 3, 10, 5, 8, 4, 3, 2]

# infinite loop
while True:
    # reading user input
    usrinput = input("index> ")
    
    # checking if user is trying to exit the program or program exit condition is true
    if (usrinput == "exit") or (len(a) == 0):
        print("quitting")
        
        # returning success error level
        exit(0)
    
    # checking if user is NaN (Not a Number)
    try:
        usrinput = int(usrinput)
    except:
        # jumping back to line 7
        print("NaN!")
        continue
    
    # checking if user input is valid index (in context of list a)
    if usrinput >= len(a):
        print("Index is out of range!")
    else:
        print(f"Element with index {usrinput} and value {a.pop(usrinput)} was removed")
    
    # outputting
    print(f"List: {a}")


