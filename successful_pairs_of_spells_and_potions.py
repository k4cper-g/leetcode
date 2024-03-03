class Solution(object):
    def successfulPairs(self, spells, potions, success):

        n = len(spells)
        m = len(potions)

        pairs = [0] * n

        potions.sort()

        for i in range(n):

            l = 0
            r = m - 1

            while l <= r:
                mid = (l + r) // 2
                comb = spells[i] * potions[mid]
                if comb >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            pairs[i] = m - l

        return pairs
