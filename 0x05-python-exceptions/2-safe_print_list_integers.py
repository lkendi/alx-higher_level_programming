#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers
    (other types of value in the list must be skipped (in silence))

    Args:
        my_list: list of values (can contain any type)
        x: number of elements of the list to print
        (can be bigger than the list length)

    Returns:
        The real number of integers printed
    """
    print_count = 0
    try:
        i = 0
        while print_count < x:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                print_count += 1
            i += 1
    except (IndexError, ValueError):
        pass
    finally:
        print()
    return print_count
