from datetime import datetime
import math
import random
from tkinter import *

# this is itre.py
A = [1, 2, 3]
B = [5, 6, 7]

def get_days(yyyy, mm, dd):
    return abs((datetime.now() - datetime(yyyy, mm, dd)).days)

def l7_3(ar):
    for var in ar:
        a = math.sin(2 * var)
        b = (2 * math.sin(var) * math.cos(var))
        print(f"Left: {a}\tRight: {b}\tDiff.: {abs(a - b)}")

def random_arr(length):
    lst = []
    for i in range(0, length):
        lst.append(random.uniform(0, 2 * math.pi))
    return lst


