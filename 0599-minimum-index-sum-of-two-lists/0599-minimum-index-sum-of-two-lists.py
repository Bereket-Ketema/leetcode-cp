class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        small = min(list1, list2)
        big = max(list1,list2)
        freq = {}
        store =[]
        for k in range(len(small)):
            if small[k] in big:
                i = k
                j = big.index(small[k])
                freq[small[k]] = i+j
        for k,v in freq.items():
            if min(freq.values()) == v:
                store.append(k)
        return store