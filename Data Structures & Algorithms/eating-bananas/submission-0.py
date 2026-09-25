class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #modulo operation
        #for each pile in piles, modulo the rating rate against the pile and add it to the hour count. if at the end the hour count is still bad binary search something something
        #k = len(piles) // 2
        #brute force solution is we try everything and mod it against each pile, sort it and index through until we find the value that is less than the threshold
        from math import ceil 

        def hours(k):
            return sum(ceil(p/k) for p in piles)

        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            if hours(mid) <= h:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo







            


