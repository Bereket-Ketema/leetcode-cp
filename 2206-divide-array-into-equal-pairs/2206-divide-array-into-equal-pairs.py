class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        store = Counter(nums)

        for i in store.values():
            if i % 2 != 0:
                return False

        return True