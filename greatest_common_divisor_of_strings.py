class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        def isDivisor(l):
            if n % l or m % l:
                return False
            f1, f2 = n//l, m//l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(n,m), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""
