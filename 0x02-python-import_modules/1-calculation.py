#!/usr/bin/python3
def main():
    import calculator_1
    a = 10
    b = 5
    sum = calculator_1.add(a, b)
    print("{} + {} = {}".format(a, b, sum))
    diff = calculator_1.sub(a, b)
    print("{} + {} = {}".format(a, b, diff))
    prod = calculator_1.mul(a, b)
    print("{} + {} = {}".format(a, b, prod))
    div = calculator_1.div(a, b)
    print("{} + {} = {}".format(a, b, div))


if __name__ == "__main__":
    main()
