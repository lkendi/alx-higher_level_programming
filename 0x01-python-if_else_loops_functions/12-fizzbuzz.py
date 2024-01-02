#!/usr/bin/python3
def fizzbuzz():
    for i in range (1, 101):
        if (i % 3 != 0 and i % 5 != 0):
            print(i, end=" ")
        else:
            str = ""
            if (i % 3 == 0):
                str += "Fizz"
            if (i % 5 == 0):
                str += "Buzz"
            print(str, end= " ")