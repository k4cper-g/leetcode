class Solution(object):
    def mergeAlternately(self, word1, word2):
        longest = max(len(word1), len(word2))

        string = []

        for i in range(longest):
            if i < len(word1):
                string.append(word1[i])
            if i < len(word2):
                string.append(word2[i])

        return ''.join(string)
