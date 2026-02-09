class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)
        for i,v in enumerate(indices):
            result[v] = s[i]
        return "".join(result)