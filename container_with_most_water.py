class Solution(object):
    def maxArea(self, height):
        
        l = 0
        r = len(height)-1

        res = 0

        while l != r:
            surf = min(height[l], height[r]) * abs(l - r)
            res = max(res, surf)
            if height[l] <= height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                continue
        
        return res
