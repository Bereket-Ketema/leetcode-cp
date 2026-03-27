class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        store = 0
        check = 0
        for i in nums:
            if i == 1:
                check += 1
            else:
                store = max(store, check)
                check = 0
        store = max(store, check)
        return store
