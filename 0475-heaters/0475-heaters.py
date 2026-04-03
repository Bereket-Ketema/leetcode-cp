from bisect import bisect_left

class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        
        for house in houses:
            idx = bisect_left(heaters, house)
            
            left_dist = float('inf') if idx == 0 else house - heaters[idx - 1]
            right_dist = float('inf') if idx == len(heaters) else heaters[idx] - house
            
            closest = min(left_dist, right_dist)
            radius = max(radius, closest)
        
        return radius