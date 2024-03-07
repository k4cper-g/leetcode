class Solution(object):
    def letterCombinations(self, digits):
        combinations = {2: ["a", "b", "c"], 3: ["d", "e", "f"],
        4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}

        n = len(digits)

        result = []

        def backtrack(i, currStr):
            if len(currStr) == n:
                result.append(currStr)
                return

            for c in combinations[int(digits[i])]:
                backtrack(i + 1, currStr + c)

        if len(digits) != 0:
            backtrack(0, "")

        return result



sol = Solution()

print(sol.letterCombinations("23"))
