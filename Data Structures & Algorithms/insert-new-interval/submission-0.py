class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        placed = False
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                output.append(interval)
            elif interval[0] > newInterval[1]:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                start = min(interval[0], newInterval[0])
                end = max(interval[1], newInterval[1])
                newInterval = [start, end]
        output.append(newInterval)
        return output
                

# Entirely left — interval[1] < newInterval[0]. Untouched; append as-is.
# Overlapping — anything not in zone 1 or 3. Don't append anything. Instead, grow newInterval: newInterval[0] = min(...), newInterval[1] = max(...). Possibly many intervals collapse here.
# Entirely right — interval[0] > newInterval[1]. Append the (now possibly grown) newInterval once, then this interval and all the rest as-is.

        #for each interval in intervals
        #if the first term of newInterval is less than the second term of interval
        #return in the output the first term of that interval as the start but we must
        #store it otherwise for the second term if it's greater than the first term of another interval we return the end of that interval
        #if there is never an overlap at all, we just insert intervals where it should go
        