class Solution:
    def getStrongest(self, arr, k):
        arr.sort()
        m = arr[(len(arr)-1)//2]
        
        arr.sort(key=lambda x:(abs(x-m),x), reverse=True)
        return arr[:k]