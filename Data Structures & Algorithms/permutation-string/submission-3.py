class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        largestring = s2
        l, r = 0, len(s1)
        smallstring = collections.Counter(s1)
        while r <= len(largestring):
            if smallstring == collections.Counter(largestring[l:r]):
                return True
            else:
                l += 1
                r += 1
        return False


