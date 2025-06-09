#include <iostream>
#include <limits.h>
using namespace std;

struct MinMax {
    int min;
    int max;
};

MinMax findMinMax(int arr[], int low, int high) {
    MinMax result, left, right;
    
    if (low == high) {
        result.min = arr[low];
        result.max = arr[low];
        return result;
    }

    if (high == low + 1) {
        if (arr[low] < arr[high]) {
            result.min = arr[low];
            result.max = arr[high];
        } else {
            result.min = arr[high];
            result.max = arr[low];
        }
        return result;
    }

    int mid = (low + high) / 2;
    left = findMinMax(arr, low, mid);
    right = findMinMax(arr, mid + 1, high);

    result.min = min(left.min, right.min);
    result.max = max(left.max, right.max);
    return result;
}

int main() {
    int arr[] = {3, 5, 1, 9, 7, 2, 8,12,1,123,5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    MinMax result = findMinMax(arr, 0, n - 1);
    cout << "Minimum element: " << result.min << endl;
    cout << "Maximum element: " << result.max << endl;
    
    return 0;
}

