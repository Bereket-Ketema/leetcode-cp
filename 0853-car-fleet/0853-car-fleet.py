class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        time = 0
        
        for pos, sp in cars:
            t = (target - pos) / sp
            if t > time:
                fleets += 1
                time = t
        
        return fleets