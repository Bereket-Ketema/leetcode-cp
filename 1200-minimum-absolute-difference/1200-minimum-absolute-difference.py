class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()

        mn = min(arr[i] - arr[i - 1] for i in range(1, len(arr)))

        ans = []

        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == mn:
                ans.append([arr[i - 1], arr[i]])

        return ans