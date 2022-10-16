#ifndef _BINARY_SEARCH_H
#define _BINARY_SEARCH_H

int BinarySearch(int arr[], int x, int low, int high)
{
    while (low <= high)
    {

        int mid = low + (high - low) / 2;

        if (arr[mid] == x)
        {
            return mid;
        }
        else if (arr[mid] < x)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return -1;
}

#endif
