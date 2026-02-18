class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = list(zip(names,heights))
        result.sort(key = lambda x: x[1], reverse = True)
        return [a for a, b in result]