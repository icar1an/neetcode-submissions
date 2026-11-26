class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            temp = [0] * 26
            for char in string:
                temp[ord(char) - ord('a')] += 1
            key = tuple(temp)
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        return list(anagrams.values())