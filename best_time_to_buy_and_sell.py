# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        max = 0

        l = 0
        r = l+1

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            elif prices[l] < prices[r] and abs(prices[l] - prices[r]) > profit:
                profit += abs(prices[l] - prices[r])
                l = r

            r += 1

        return profit


sol = Solution()

print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
