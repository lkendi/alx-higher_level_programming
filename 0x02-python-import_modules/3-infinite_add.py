#!/usr/bin/python3
def main():
    import sys
    argv = sys.argv
    if (len(argv) > 1):
        total = sum(int(arg) for arg in argv[1:])
        return (total)
    else:
        return (0)


if __name__ == "__main__":
    print(main())
