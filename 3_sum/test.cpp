#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> nums = {3, 0, -2, -1, 1, 2};
    sort(nums.begin(), nums.end());
    int sz = nums.size();
    vector<vector<int>> ans;

    for (int i = 0; i < sz - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1])
            continue; // Skip duplicates

        int left = i + 1;
        int right = sz - 1;

        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];

            if (sum == 0) {
                ans.push_back({nums[i], nums[left], nums[right]});
                while (left < right && nums[left] == nums[left + 1])
                    left++; // Skip duplicates
                while (left < right && nums[right] == nums[right - 1])
                    right--; // Skip duplicates
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

   
}
