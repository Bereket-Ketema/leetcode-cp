MOD = 10**9+7

class Fancy:

    def __init__(self):
        self.arr = []
        self.mul = 1
        self.add = 0

    def append(self, val):
        inv = pow(self.mul, MOD-2, MOD)
        self.arr.append((val-self.add)*inv % MOD)

    def addAll(self, inc):
        self.add = (self.add + inc) % MOD

    def multAll(self, m):
        self.mul = self.mul * m % MOD
        self.add = self.add * m % MOD

    def getIndex(self, idx):
        if idx >= len(self.arr):
            return -1
        
        return (self.arr[idx]*self.mul + self.add) % MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)