class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)

        res = [0]*n

        stack = []

        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])

        return res
