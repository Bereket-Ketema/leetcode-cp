class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        freq = {}
        result = []
        small = len(list1) + len(list2)
        for k in range(len(list1)):
                freq[list1[k]] = k
        for i in range(len(list2)):
            if list2[i] in freq:
                s = i + freq[list2[i]]
                if s < small:
                        small = s
                        result = [list2[i]]
                elif s == small:
                    result.append(list2[i])
        return result