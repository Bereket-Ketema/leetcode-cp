class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        childs = [0] * k
        self.minUnfairness = float('inf')

        def backtrack(idx):
            if idx == len(cookies):
                self.minUnfairness = min(self.minUnfairness, max(childs))
                return
            
            for i in range(k):
                if childs[i] >= self.minUnfairness:
                    continue

                childs[i] += cookies[idx]
                backtrack(idx + 1)
                childs[i] -= cookies[idx]

                if childs[i] == 0:
                    break

        backtrack(0)
        return self.minUnfairness