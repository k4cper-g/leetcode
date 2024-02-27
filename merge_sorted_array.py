# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index = 0
        for i, num in enumerate(reversed(nums1)):
            if i >= m:
                nums1[i] = nums2[index]
                index+=1

        nums1.sort()
        print(nums1)
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

sol = Solution()

sol.merge([-1,0,0,3,3,3,0,0,0],6, [1,2,2], 3)
