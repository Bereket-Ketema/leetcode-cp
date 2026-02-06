class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for word in strs:
            store["".join(sorted(word))].append(word)
        return [v for v in store.values()]