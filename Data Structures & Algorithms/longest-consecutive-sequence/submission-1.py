class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set()
        longest = 1
        current = 1
        if nums == []:
            return 0
        for num in nums:
            hash.add(num)
        for num in hash:
            if (num-1) not in hash:
                current = 1
                while num + current in hash:
                    current += 1
                    if current > longest:
                        longest = current
        return longest

        