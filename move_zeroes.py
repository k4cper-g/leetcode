class Solution(object):
    def moveZeroes(self, nums):

        n = len(nums)

        if n < 2:
            return nums

        l = n - 2
        r = n - 1

        while l >= 0:

            if nums[l] == 0 and nums[r] != 0:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp

                if r < n - 1:
                    l += 1
                    r += 1

            else:
                l -= 1
                r -= 1

        return nums
