class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]
        ans = []

        def backtrack(idx, combination):
            if len(combination) == k:
                ans.append(combination[:]) #copy
                return
            
            if idx == len(arr):
                return

            combination.append(arr[idx])
            backtrack(idx + 1, combination)

            combination.pop()
            backtrack(idx + 1, combination)

        backtrack(0, [])
        return ans