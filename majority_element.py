# Given an array nums of size n, return the majority element.
# 
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# 
# You may assume that the majority element always exists in the array.


class Solution(object):
    def majorityElement(self, nums):
        for num in nums:
            if nums.count(num) > len(nums) / 2:
                return num

        """
        :type nums: List[int]
        :rtype: int
        """


sol = Solution()

print(sol.majorityElement([3,2,3]))
