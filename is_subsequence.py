# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# 
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of 
# the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, s, t):

        if len(s) > len(t):
            return False

        si = 0
        ti = 0

        count = 0

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
                count += 1
            ti += 1

        return count == len(s)





sol = Solution()

print(sol.isSubsequence("aaba", "aaaadababaaaaaa"))
