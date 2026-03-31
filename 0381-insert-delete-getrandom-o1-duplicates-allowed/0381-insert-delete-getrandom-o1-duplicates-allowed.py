class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.idx_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.idx_map[val].add(len(self.nums) - 1)
        return len(self.idx_map[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx_map[val]:
            return False
        
        remove_idx = self.idx_map[val].pop()
        last_val = self.nums[-1]

        self.nums[remove_idx] = last_val
        self.idx_map[last_val].add(remove_idx)
        self.idx_map[last_val].discard(len(self.nums) - 1)

        self.nums.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)