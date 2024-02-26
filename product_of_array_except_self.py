# Given an integer array nums,
# return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        left = [0] * length
        left[0] = 1

        right = [0] * length
        right[-1] = 1
        #
        # for i in range(1, length):
        #     r = right[i+1]
        #     n = nums[i+1]
        #     right[i] = r * n

        for i in range(1, length):
            l = left[i - 1]
            n = nums[i - 1]
            left[i] = l * n

        for j in range(length - 2, -1, -1):
            r = right[j + 1]
            n = nums[j + 1]
            right[j] = r * n

        product = []
        for k in range(0, length):
            product.append(left[k] * right[k])

        return product


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
