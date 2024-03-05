class Solution(object):
    def maxOperations(self, nums, k):
        n = len(nums)

        l = 0
        r = n-1

        nums.sort()

        operation = 0

        while l < r:
            sm = nums[l] + nums[r]
            if sm == k:
                operation += 1
                l += 1
                r -= 1
            elif sm < k:
                l += 1
            else:
                r -= 1
        
        return operation
