class Solution(object):
    def longestConsecutive(self, nums):

        if len(nums) == 0:
            return 0

        nums.sort()

        consecutive = 0
        count = 1

        for i in range(1, len(nums)):
            if nums[i] !=  nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    count += 1
                else:
                    consecutive = max(consecutive, count)
                    count = 1
        return max(consecutive, count)
