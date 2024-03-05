class Solution(object):
    def uniqueOccurrences(self, arr):
        
        mp = dict()

        for i in range(len(arr)):
            if arr[i] not in mp:
                mp[arr[i]] = 1
            else:
                mp[arr[i]] += 1
        
        s = set(mp.values())

        return list(sorted(s)) == sorted(mp.values())
