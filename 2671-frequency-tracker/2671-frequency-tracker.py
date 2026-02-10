from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.freq = [0]*200000
        self.store = defaultdict(int)
        

    def add(self, number: int) -> None:
        if self.freq[self.store[number]] != 0:
            self.freq[self.store[number]] -= 1
        self.store[number] += 1
        self.freq[self.store[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.store[number] != 0:
            if self.freq[self.store[number]] != 0:
              self.freq[self.store[number]] -= 1
            self.store[number] -= 1
            if self.store[number] == 0:
                del self.store[number]
            else:
                self.freq[self.store[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return  self.freq[frequency] > 0