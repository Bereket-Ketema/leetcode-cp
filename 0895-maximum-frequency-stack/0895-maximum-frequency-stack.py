from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxf = 0
    
    def push(self, val):
        f = self.freq[val] + 1
        self.freq[val] = f
        self.maxf = max(self.maxf, f)
        self.group[f].append(val)
    
    def pop(self):
        val = self.group[self.maxf].pop()
        self.freq[val] -= 1
        if not self.group[self.maxf]:
            self.maxf -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()