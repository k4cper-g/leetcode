class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        m = {}
        
        if n < 2:
            return nums
        
        for i in range(n):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1

        res = []
        
        for i in range(0, k):
            mx = max(m, key=m.get)
            if mx not in res:
                res.append(mx)
            del m[mx]

        
        return res
