class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        store = []
        freq = Counter(arr1)
        for i in arr2:
            for j in range(freq[i]):
                store.append(i)
                arr1.remove(i)
        
        arr1.sort()

        for i in arr1:
            store.append(i)
        return store
        