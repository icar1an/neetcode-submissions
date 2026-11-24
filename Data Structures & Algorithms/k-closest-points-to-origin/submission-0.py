class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            distance = -1 * ((point[0] ** 2) + (point[1] ** 2))
            if len(h) < k:
                heapq.heappush(h, (distance, point))
            else:
                if distance > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (distance, point))
        return [p for _, p in h]

        


