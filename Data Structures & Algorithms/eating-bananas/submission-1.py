class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(pile, k):
            if pile % k == 0:
                return pile // k
            else:
                return (pile // k) + 1

        def feasible(k):
            count = 0
            for pile in piles:
                count += hours(pile, k)
            return count <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
        
        
