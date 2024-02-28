# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""

        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or str[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
        """
        :type strs: List[str]
        :rtype: str
        """


sol = Solution()

print(sol.longestCommonPrefix(["flower","flow","flight"]))
