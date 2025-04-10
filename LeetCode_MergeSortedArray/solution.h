#include <iostream>
#include <vector>

class Solution
{
public:
    void merge(std::vector<int> &nums1, int m, std::vector<int> &nums2, int n)
    {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        while (i >= 0 && j >= 0)
        {
            if (nums1[i] > nums2[j])
            {
                nums1[k] = nums1[i];
                i--;
                k--;
            }
            else
            {
                nums1[k] = nums2[j];
                j--;
                k--;
            }
        }

        while (i >= 0)
        {
            std::cout << "iter i = " << i << ":" << std::endl;
            std::cout << "BEFORE k--: nums1[k--] = " << nums1[k] << std::endl;
            std::cout << "k = " << k << std::endl;

            nums1[k--] = nums1[i--];

            std::cout << "AFTER k--: nums1[k--] = " << nums1[k] << std::endl;
            std::cout << "After [i--] and BEFORE next while loop iter: " << i
                      << std::endl;
            std::cout << "k = " << k << std::endl;
        }
        while (j >= 0)
        {
            std::cout << "iter j = " << j << ":" << std::endl;
            nums1[k--] = nums2[j--];
            std::cout << "After [j--] and BEFORE next while loop iter: " << j
                      << std::endl;
        }

        // std::cout << "End of merge(): nums1 = " << nums1 << std::endl;
    }
};