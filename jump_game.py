class Solution(object):
    def canJump(self, nums):

        val = 0

        for num in nums:
            if val < 0:
                return False
            elif num > val:
                val = num
                
            val -= 1
        return True
