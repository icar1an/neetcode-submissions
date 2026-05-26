class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmaps = {}
        final = []
        for str in strs:
            strmap = {}
            for char in str:
                if char in strmap:
                    strmap[char] += 1
                else:
                    strmap[char] = 1
            key = tuple(sorted(strmap.items()))
            if key in strmaps:
                strmaps[key].append(str)
            else:
                strmaps[key] = [str] 
        for item in strmaps.values():
            final.append(item)
        return final

            

                

