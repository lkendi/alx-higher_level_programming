#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list, handling potential errors.

    Args:
        my_list: The list to print from.
        x: The number of elements to print
        (can be larger than the list length).

    Returns:
        The actual number of elements printed
    """
    print_count = 0
    try:
        i = 0
        while i < x:
            try:
                print(my_list[i], end="")
                print_count += 1
            except IndexError:
                break
            i += 1
    finally:
        print()
    return print_count
