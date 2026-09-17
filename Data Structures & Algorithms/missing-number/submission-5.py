class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        numset = {x for x in range(n)}
        newset = set(nums)
        return (numset - newset).pop()
        
        
        
        
             
        