class Solution:
    def rob(self, nums: List[int]) -> int:
        loot = [-1] * len(nums)

        def dfs(i):
            if i>=len(nums):
                return 0
            if loot[i] != -1:
                return loot[i]
            loot[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return loot[i]
        
        return dfs(0)