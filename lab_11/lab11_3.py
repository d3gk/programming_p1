
import numpy as np

def main():
    f = open("sin_table.txt", "w")
    res = ""
    i = 0
    while i < 370:
        res += f"{i:03} - {np.sin(np.deg2rad(i)):.3f}\n"
        print(f"{i:03} - {np.sin(np.deg2rad(i)):.3f}")
        i += 10
    f.write(res)
    f.close()

if __name__ == "__main__":
    main()
    
