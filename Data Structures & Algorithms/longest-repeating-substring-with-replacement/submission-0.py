class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        longest = 0
        l, r = 0, 0
        for r in range(len(s)):
            char = s[r]
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
            maxcount = max(counts.values())
            while (r - l + 1) - maxcount > k:
                counts[s[l]] -= 1
                l += 1
                maxcount = max(counts.values())
            longest = max(longest, r - l + 1)
        return longest







        