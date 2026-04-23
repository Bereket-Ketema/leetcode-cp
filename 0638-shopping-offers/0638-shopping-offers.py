class Solution:
    def shoppingOffers(self, price, special, needs):
        memo = {}
        
        def dfs(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]
            
            res = sum(needs[i] * price[i] for i in range(len(needs)))
            
            for sp in special:
                new_needs = []
                for i in range(len(needs)):
                    if sp[i] > needs[i]:
                        break
                    new_needs.append(needs[i] - sp[i])
                else:
                    res = min(res, sp[-1] + dfs(new_needs))
            
            memo[tuple(needs)] = res
            return res
        
        return dfs(needs)