class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        store = set(arr)
        count = 0
        for i in range(1, arr[-1] + k+1):
            if i not in store:
                count += 1
            if count == k:
                return i