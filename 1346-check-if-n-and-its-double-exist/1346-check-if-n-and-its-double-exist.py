class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        store = set(arr)
        for num in arr:
            if num != 1 and num != 0:
                if (num * 2) in store:
                    return True
            elif freq[num] > 1:
                return True
        return False                