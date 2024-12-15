
a = [7, 5, 4, 3, -3, 10, -13, 37]
b = []

def main():
    for n in a:
        if n > 0:
            b.append(n * 2)
        else:
            b.append(0)
    print(b)

if __name__ == "__main__":
    main()
    
    
    