class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l:int, r:int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        longest = ""
        for idx, char in enumerate(s):
            odd = expand(idx, idx)
            even = expand(idx, idx+1)
            longest = max(longest, odd, even, key=len)
        return longest 

            
                

