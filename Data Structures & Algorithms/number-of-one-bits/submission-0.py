class Solution:
    def hammingWeight(self, n: int) -> int:
        result = bin(n)
        count = 0
        for char in result:
            if char == "1":
                count += 1
        return count

