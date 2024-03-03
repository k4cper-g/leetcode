import math


class Solution(object):
    def minEatingSpeed(self, piles, h):

        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = (l+r) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k+1

        return res
