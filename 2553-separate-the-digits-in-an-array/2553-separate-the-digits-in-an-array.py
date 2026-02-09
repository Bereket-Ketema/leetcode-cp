class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        store = ""
        for i in nums:
            store += str(i)
        return [int(n) for n in store]