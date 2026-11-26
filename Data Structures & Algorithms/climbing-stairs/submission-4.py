class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n

        def dfs(n):
            if n == 1:
                return 1
            if n == 2: 
                return 2
            if memo[n-1] != -1:
                return memo[n-1]
            memo[n-1] = dfs(n-1) + dfs(n-2)
            return memo[n-1]

        return dfs(n)