class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = target
        situation = [0] * n
        for idx, car in enumerate(position):
            situation[car] = speed[idx]
        lead_time = None
        fleetcount = 0
        while situation:
            val = situation.pop()
            if val == 0:
                continue
            position = len(situation)
            t = (target - len(situation))/val
            if lead_time is None or t > lead_time:
                fleetcount += 1
                lead_time = t
        return fleetcount



