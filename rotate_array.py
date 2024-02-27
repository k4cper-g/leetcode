# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
    # def rotate(self, nums, k):
    #     rotation = []
    #     for i in range(0, k):
    #         rotation = [0] * len(nums)
    #         for j, num in enumerate(nums):
    #             if j == len(nums)-1:
    #                 rotation[0] = nums[j]
    #                 break
    #             rotation[j+1] = nums[j]
    #         nums = rotation
    #
    #     for i in range(len(nums)):
    #         nums[i] = rotation[i]
    #     print(nums)

    def reverse(self, nums, left, right):
        left = left
        right = right

        while left < right:
            tmp = nums[right]
            nums[right] = nums[left]
            nums[left] = tmp
            left += 1
            right -= 1
        print(nums)

        return nums

    def rotate(self, nums, k):
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - 1 - k)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """


sol = Solution()

print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))
