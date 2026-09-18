class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        testset = set()
        for n in nums:
            testset.add(n)
        if len(testset) != len(nums):
            return True
        else:
            return False
        
        