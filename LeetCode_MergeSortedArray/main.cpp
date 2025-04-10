#include "solution.h"
#include <iostream>
#include <vector>

int main()
{
    std::cout << "Hello World!\n";

    Solution s = Solution();
    std::vector<int> nums1 = {1, 2, 3, 0, 0, 0};
    std::vector<int> nums2 = {2, 5, 6};
    s.merge(nums1, 3, nums2, 3);
}