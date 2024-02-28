# Given a pattern and a string s, find if s follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = []
        map2 = []

        splitted = s.split()

        for idx in pattern:
            map1.append(pattern.index(idx))
            print(map1)
        for idx in splitted:
            map2.append(splitted.index(idx))
            print(map2)
        if map1 == map2:
            return True
        return False


sol = Solution()

print(sol.wordPattern("abba", "dog cat cat dog"))
