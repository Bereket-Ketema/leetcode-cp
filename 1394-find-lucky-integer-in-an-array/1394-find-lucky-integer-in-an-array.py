from collections import Counter

class Solution:
    def findLucky(self, arr):
        c = Counter(arr)
        ans = -1

        for num,freq in c.items():
            if num == freq:
                ans = max(ans,num)

        return ans