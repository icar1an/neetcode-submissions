class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        result = []
        for i in range(len(nums)):
            current_element = nums[i]
            remaining_elements = nums[:i] + nums[i+1:]

            for p in self.permute(remaining_elements):
                result.append([current_element] + p)
        return result
                
