import os
from tkinter import *
from tkinter import messagebox


def main():
    Input()
 
def Input():
    count = int(input("ราคาสินค้า : "))
    discount = int(input("ส่วนลด : "))
    Process(count,discount)

def Process(C,D):
    total1 = C * D  / 100
    total2 = C - total1
    print(total2)

main()