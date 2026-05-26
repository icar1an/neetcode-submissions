class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return True
            elif i not in hashmap:
                hashmap[i] = i
        return False