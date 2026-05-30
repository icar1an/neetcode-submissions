class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for idx, num in enumerate(nums):
            i = idx + 1
            j = len(nums) - 1
            if idx > 0 and num == nums[idx - 1]:
                continue
            while i < j:
                if nums[i] + nums[j] + num == 0:
                    output.append([nums[i], nums[j], num])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    if nums[i] + nums[j] + num > 0:
                        j -= 1
                    elif nums[i] + nums[j] + num < 0:
                        i += 1
        return output





            