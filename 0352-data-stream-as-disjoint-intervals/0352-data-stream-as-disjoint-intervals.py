class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        new = [value, value]
        res = []
        placed = False
        
        for interval in self.intervals:
            if interval[1] + 1 < value:
                res.append(interval)
            elif value + 1 < interval[0]:
                if not placed:
                    res.append(new)
                    placed = True
                res.append(interval)
            else:
                new[0] = min(new[0], interval[0])
                new[1] = max(new[1], interval[1])
        
        if not placed:
            res.append(new)
        
        self.intervals = res

    def getIntervals(self):
        return self.intervals