import random
class RandomizedSet:

    def __init__(self):
        self.freq = {}
        self.store = []
        

    def insert(self, val: int) -> bool:
        if val not in self.freq:
            self.store.append(val)
            self.freq[val] = len(self.store)-1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.freq:
            self.store.remove(val)
            del self.freq[val]
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(self.store)