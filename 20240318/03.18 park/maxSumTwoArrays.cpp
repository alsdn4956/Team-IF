#include <iostream>
#include <vector>
using namespace std;

int maxSumTwoArrays(vector<int>& nums1, vector<int>& nums2) {
    int maxSum = 0;
    int maxNum1 = *max_element(nums1.begin(), nums1.end());
    int maxNum2 = *max_element(nums2.begin(), nums2.end());

    maxSum = maxNum1 + maxNum2;

    return maxSum;
}

int main() {
    vector<int> nums1 = {1, 4, 6, 8};
    vector<int> nums2 = {3, 5, 7};

    int result = maxSumTwoArrays(nums1, nums2);
    cout << "두 배열에서 선택된 요소들의 최대 합: " << result << endl;

    return 0;
}
