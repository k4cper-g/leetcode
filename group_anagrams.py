class Solution(object):
    def groupAnagrams(self, strs):
        m = {}

        for i in range(len(strs)):
            srtd = ''.join(sorted(strs[i]))

            if srtd in m:
                m[srtd].append(strs[i])
            else:
                m[srtd] = [strs[i]]

        return m.values()
        
