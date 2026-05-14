class MyHashSet:

    def __init__(self):
        self.s = set()

    def add(self, key):
        self.s.add(key)

    def remove(self, key):
        self.s.discard(key)

    def contains(self, key):
        return key in self.s

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)