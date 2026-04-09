from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.minf = 0
        self.val = {}
        self.freq = {}
        self.group = defaultdict(OrderedDict)

    def _update(self, key):
        f = self.freq[key]
        del self.group[f][key]
        if not self.group[f]:
            if f == self.minf:
                self.minf += 1
        self.freq[key] += 1
        self.group[f+1][key] = None

    def get(self, key: int) -> int:
        if key not in self.val:
            return -1
        self._update(key)
        return self.val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.val:
            self.val[key] = value
            self._update(key)
            return
        
        if len(self.val) == self.cap:
            k, _ = self.group[self.minf].popitem(last=False)
            del self.val[k]
            del self.freq[k]
        
        self.val[key] = value
        self.freq[key] = 1
        self.group[1][key] = None
        self.minf = 1