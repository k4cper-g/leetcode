class Solution(object):
    def reverseVowels(self, s):
        n = len(s)

        arr = list(s)

        vowels = ['a', 'e', 'i', 'o', 'u']

        l = 0
        r = n - 1

        while l <= r:
            if arr[l].lower() in vowels and arr[r].lower() in vowels:
                tmp = arr[l]
                arr[l] = arr[r]
                arr[r] = tmp

                l += 1
                r -= 1

            if arr[l].lower() not in vowels:
                l += 1
            elif arr[r].lower() not in vowels:
                r -= 1
        return ''.join(arr)
