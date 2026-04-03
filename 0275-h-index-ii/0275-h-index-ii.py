class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        store = [0] * (len(citations) + 1)
        for num in citations:
            if num < len(citations):
                store[num] += 1
            else:
                store[len(citations)] += 1
        paper = 0
        for i in range(len(citations),-1,-1):
            paper += store[i]
            if paper >= i:
                return i