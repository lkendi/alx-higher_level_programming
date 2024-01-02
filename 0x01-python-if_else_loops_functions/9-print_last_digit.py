#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number *= -1
        last = -1 * (number % 10)
    else:
        last = number % 10
    print(last, end="")
    return last

