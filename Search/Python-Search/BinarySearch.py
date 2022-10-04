def binary_search(arr, a, low, high):

    # Repeat until low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if arr[mid] == a:
            return mid

        elif array[mid] < a:
            low = mid + 1

        else:
            high = mid - 1

    return -1
