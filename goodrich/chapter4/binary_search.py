def binary_search(data, target, low, high):
    """
    Simple binary search recursive function.
    Need to provide low and high as border indices
    """
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


def binary_search_whole_array(arr, target):
    """
    Call recursive function with across the list

    >>> binary_search_whole_array(range(10), 5)
    5

    >>> binary_search_whole_array('binary_search', '_')
    6
    """
    return binary_search(arr, target, 0, len(arr))
