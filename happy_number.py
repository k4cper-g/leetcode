# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution(object):
    def isHappy(self, n):
        st = list(str(n))

        cycle = set()

        target = n

        while target != 1:
            sum = 0
            st = list(str(target))
            for i in range(len(st)):
                sum += pow(int(st[i]), 2)
            if sum in cycle:
                return False
            target = sum
            cycle.add(sum)
        return True


sol = Solution()

print(sol.isHappy(18))
