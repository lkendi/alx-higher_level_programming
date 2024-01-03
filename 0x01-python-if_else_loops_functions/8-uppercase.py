#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if (ord(char) >= 97 and ord(char) <= 122):
            new = ord(char) - 32
            result += chr(new)
        else:
            result += char
    print(result, end="\n")
