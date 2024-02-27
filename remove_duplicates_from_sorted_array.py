# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
#
# Return k.

class Solution(object):
    def removeDuplicates(self, nums):
        j = 1
        print(nums)

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
                print(nums)

        return j

        """
        :type nums: List[int]
        :rtype: int
        """


sol = Solution()

print(sol.removeDuplicates([1, 1, 2, 4, 5, 5, 5]))
