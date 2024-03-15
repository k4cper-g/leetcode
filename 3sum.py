class Solution(object):
    def threeSum(self, nums):
        n = len(nums)

        nums.sort()

        sol = []


        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm == 0:
                    if [nums[i], nums[l], nums[r]] not in sol:
                        sol.append([nums[i], nums[l], nums[r]])
                if sm < 0:
                    l += 1
                else:
                    r -= 1
        return sol

