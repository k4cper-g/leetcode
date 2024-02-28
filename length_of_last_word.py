class Solution(object):
    def lengthOfLastWord(self, s):
        return len(list(s.split()[-1:][0]))


sol = Solution()

print(sol.lengthOfLastWord("luffy is still joyboy")
