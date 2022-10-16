int BinarySearch(int arr[], int a, int low, int high)
{
    while (low <= high)
    {

        int mid = low + (high - low) / 2;

        if (arr[mid] == a)
        {
            return mid;
        }
        else if (arr[mid] < a)
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
