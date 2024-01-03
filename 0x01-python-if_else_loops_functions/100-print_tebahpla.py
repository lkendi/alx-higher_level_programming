#!/usr/bin/python3
for a in range(122, 96, -1):
    if (a % 2 != 0):
        print(chr(a - 32), end="")
    else:
        print(chr(a), end="")