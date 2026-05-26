class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}
        for letter in s:
            if letter in hashs:
                hashs[letter] += 1
            elif letter not in hashs:
                hashs[letter] = 1
        for letter in t:
            if letter in hasht:
                hasht[letter] += 1
            elif letter not in hasht:
                hasht[letter] = 1
        if hashs == hasht:
            return True
        elif hashs != hasht:
            return False
        