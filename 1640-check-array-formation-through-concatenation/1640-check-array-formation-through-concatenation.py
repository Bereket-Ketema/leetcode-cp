class Solution:
    def canFormArray(self, arr, pieces):
        mp = {}

        for p in pieces:
            mp[p[0]] = p

        i = 0

        while i < len(arr):
            if arr[i] not in mp:
                return False

            piece = mp[arr[i]]

            for x in piece:
                if i >= len(arr) or arr[i] != x:
                    return False
                i += 1

        return True