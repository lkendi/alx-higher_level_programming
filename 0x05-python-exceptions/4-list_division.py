#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element in 2 lists

    Args:
        my_list_1: first list (can contain any type)
        my_list_2: second list(can contain any type)
        list_length: length of the list (can be bigger
        than the length of both lists)

    Returns:
        A new list(length = list_length) with all division
    """
    try:
        result = []
        for i in range(list_length):
            result.append(my_list_1[i] / my_list_2[i])
    except TypeError:
        print("wrong type")
        result.append(0)
    except ZeroDivisionError:
        print("division by 0")
        result.append(0)
    except IndexError:
        print("out of range")
        result.append(0)
    finally:
        return result
