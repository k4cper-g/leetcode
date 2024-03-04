class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []

        most = max(candies)

        for candy in candies:
            if candy+extraCandies >= most:
                result.append(True)
            else:
                result.append(False)

        return result
