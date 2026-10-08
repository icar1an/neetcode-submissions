class TimeMap:

    def __init__(self):
        self.storage = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
            self.storage[key].append((timestamp, value))
        else:
            self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        searchspace = self.storage[key]
        lo, hi = 0, len(searchspace)
        while lo < hi:
            mid = (lo + hi) // 2
            if searchspace[mid][0] <= timestamp:
                lo = mid + 1
            else:
                hi = mid
        if lo == 0:
            return ""
        else:
            return searchspace[lo-1][1]
