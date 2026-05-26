class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        flatmap = list(sorted(hashmap.items(), key=lambda item: item[1]))
        output = []
        count = -1
        for i in range(k):
            output.append(flatmap[count][0])
            count -= 1
        return output
