class Solution(object):
    def largestAltitude(self, gain):

        mx = 0
        sum = 0
        
        for g in gain:
            sum += g
            mx = max(sum, mx)
        
        return mx
