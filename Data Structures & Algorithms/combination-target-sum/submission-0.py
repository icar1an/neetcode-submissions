
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def subsets(nums: List[int]) -> List[List[int]]:
            res = []

            subset = []
            def dfs(i, total):
                if total == target:
                    res.append(subset.copy())
                    return
                if i >= len(nums) or total > target:
                    return

                #decision to include nums[i]
                subset.append(nums[i])
                dfs(i, total + nums[i])

                #decision NOT to include nums[i]
                subset.pop()
                dfs(i+1, total)

            dfs(0, 0)
            return res
        
        return subsets(nums)
