class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        results = [0] * n
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                results[j] = i-j
            stack.append(i)
        return results




            





