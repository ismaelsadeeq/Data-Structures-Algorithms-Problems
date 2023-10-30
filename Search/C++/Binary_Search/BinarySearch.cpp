#include <iostream>
#include <vector>

using namespace std;

int binary_search(vector<int> &numbers, int value)
{
    int left = 0, right = numbers.size() - 1;
    while(left <= right) {
        int i = (left + (right - left) / 2);
        if (numbers[i] == value) {
            return i; 
        }
        if (numbers[i] < value) {
            left = i + 1;
        }else {
            right = i -1;
        }
    }
    return -1;

}

int main() {

    vector<int> nums{1,2,3,4,5,6,7,8,9,10};
    vector<int> values{2, 4, 20};

    for (int val : values) {
        int index = binary_search(nums, val);
        if (index != -1) {
            cout << "Value " << val << " exists in index " << index << endl;
        } else {
            cout << "Value " << val << " does not exist." << endl;
        }
    }

}