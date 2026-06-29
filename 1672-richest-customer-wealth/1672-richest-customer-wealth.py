class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        store = sum(accounts[0])

        for i in range(1, len(accounts)):
            store = max(store, sum(accounts[i]))

        return store