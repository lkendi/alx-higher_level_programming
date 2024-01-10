#!/usr/bin/python3
import marshal


def main():
    with open('hidden_4.pyc', 'rb') as file:
        contents = file.read()
        obj = marshal.loads(contents[16:])
        names = obj.co_names
        names_sorted = sorted(names)
        for name in names_sorted:
            if not name.startswith('__'):
                print(name)


if __name__ == "__main__":
    main()
