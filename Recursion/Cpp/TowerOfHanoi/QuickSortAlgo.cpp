#include <bits/stdc++.h>
using namespace std;

int partition(int a[], int s, int e)
{
    int pivot = a[e];
    int i = s - 1;
    for (int j = s; j < e; j++)
    {
        if (a[j] < pivot)
        {
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[i + 1], a[e]);
    return i + 1;
}

void quicksort(int a[], int s, int e)
{
    // Base case
    if (s >= e)
    {
        return;
    }

    // Recursive case
    int p = partition(a, s, e);
    quicksort(a, s, p - 1);
    quicksort(a, p + 1, e);
}

int main()
{
    int n;
    cout << "Please enter the size of the array: ";
    cin >> n;

    int a[n];

    cout << "Please input the elements of the array you want to sort: " << endl;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    quicksort(a, 0, n - 1);

    cout << "The required sorted array is: " << endl;

    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }

    return 0;
}
