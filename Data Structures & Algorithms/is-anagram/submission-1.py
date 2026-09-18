class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {}
        tdict = {}
        for i in range(len(s)):
            if s[i] in sdict:
                sdict[s[i]] += 1
            else:
                sdict[s[i]] = 1
            if t[i] in tdict:
                tdict[t[i]] += 1
            else:
                tdict[t[i]] = 1
        return sdict == tdict

        # n = len(s)
        # i, j = 0, n - 1
        # while i != j:
        #     if s[i] != t[j]:
        #         return False
        #     else:
        #         i += 1
        #         j -= 1
        # return True