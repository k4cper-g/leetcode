# Given an integer array nums and an integer k,
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        map = {}

        for i in range(len(nums)):
            if nums[i] in map:
                if abs(map[nums[i]] - i) <= k:
                    return True
            map[nums[i]] = i

        return False


sol = Solution()

print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))
