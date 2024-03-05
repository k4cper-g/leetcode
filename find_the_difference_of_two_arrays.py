class Solution(object):
    def findDifference(self, nums1, nums2):

        s1 = set(nums1)
        s2 = set(nums2)

        diff1 = list(s1 - s2)
        diff2 = list(s2 - s1)

        return [diff1, diff2]
