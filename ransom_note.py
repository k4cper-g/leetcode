# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        map = {}

        for note in ransomNote:
            map.update({note: ransomNote.count(note)})

        for mag in magazine:
            if mag in map:
                print(map)
                map.update({mag: map.get(mag) - 1})
                print(map)

        if all(value == 0 for value in map.values()):
            return True
        else:
            return False


sol = Solution()

print(sol.canConstruct("", ""))
