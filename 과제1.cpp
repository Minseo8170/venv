#include <iostream>
#include <vector>
using namespace std;

int bubbleSortAndCountSwaps(vector<int>& arr) {
    int n = arr.size();
    int swapCount = 0;

    for (int i = 0; i < n - 1; ++i) {
        // 각 패스마다
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                // 인접한 두 수를 비교하여 필요 시 교환
                swap(arr[j], arr[j + 1]);
                ++swapCount; // 교환 횟수 증가
            }
        }
    }

    return swapCount;
}

int main() {
    int n;
    cin >> n; // 배열 크기 입력

    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i]; // 배열 요소 입력
    }

    int result = bubbleSortAndCountSwaps(arr);
    cout << result << endl; // 교환 횟수 출력

    return 0;
}
