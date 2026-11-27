class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dfs(i, n, memo):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + dfs(i+2, n, memo), dfs(i+1, n, memo))
            return memo[i]
        
        return max(dfs(0, len(nums)-1, [-1]*len(nums)), dfs(1, len(nums), [-1]*len(nums)))