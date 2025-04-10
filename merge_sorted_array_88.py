class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
        """


        # Brute Force Approach:
        # Nested for-loop, where we compare each number in nums2 to each one in nums1 and see where we can insert each nums2 element into nums1.

        # Problem with Brute Force Approach:
        # Time Complexity of O(n^2) due to the nested for-loops
        # (Not very fast and time efficient)
        # Therefore, I plan to steer away from using nested for-loops.

        # A Better Solution would be:
        # Two-Pointer Method (one pointer for each array), and Reverse Sorting (starting and adding larger numbers to the end of nums1 array, and decrementing each pointer as we move along).
        # This is because arrays nums1 and nums2 are already sorted in non-decreasing order.
        # Variable k will be at the last position of k=(nums1.length)+(nums2.length)-1
        # We will check for larger elements (between nums1 and nums2 arrays), and insert the larger element to where variable k is (combined size of nums1 and nums2 arrays)

        k = m + n - 1
        index_nums1 = m - 1
        index_nums2 = n - 1

        while index_nums2 >= 0:
            if index_nums1 >= 0 and nums1[index_nums1] > nums2[index_nums2]:
                nums1[k] = nums1[index_nums1]
                index_nums1 -= 1
            else:
                nums1[k] = nums2[index_nums2]
                index_nums2 -= 1
            k -= 1