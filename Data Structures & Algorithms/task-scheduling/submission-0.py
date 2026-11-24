class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = dict(Counter(tasks))
        h = [-val for val in frequency.values()]
        heapq.heapify(h)

        time = 0
        while h:
            temp = []
            for _ in range(n+1):
                if not h:
                    break
                task = heapq.heappop(h)
                task += 1
                temp.append(task)
            
            ran = len(temp)
            for t in temp:
                if t < 0:
                    heapq.heappush(h, t)
            time += (n+1 if h else ran)

        return time





        