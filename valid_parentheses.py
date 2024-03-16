class Solution(object):
    def isValid(self, s):
        m = {')': '(', '}': '{', ']': '['}
        n = len(s)

        stack = []

        for i in range(n):
            if s[i] in m:
                if stack and stack[-1] == m[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return True if not stack else False
