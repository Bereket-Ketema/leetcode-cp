class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0

        for x, c in count.items():
            group_size = x + 1
            groups = ceil(c / group_size)
            total += groups * group_size
        
        return total