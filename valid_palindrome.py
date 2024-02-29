# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):

        clean = []

        for i in range(len(s)):
            if s[i].isalnum():
                clean.append(s[i].lower())

        return clean == list(reversed(clean))


sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))
