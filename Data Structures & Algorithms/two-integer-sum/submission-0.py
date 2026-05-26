class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, i in enumerate(nums):
            if (target - i) in hashmap:
                return [min(hashmap[target-i], idx), max(hashmap[target-i], idx)]
            hashmap[i] = idx
            
