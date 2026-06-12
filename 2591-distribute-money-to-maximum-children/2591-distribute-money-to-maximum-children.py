class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        
        if money < 0:
            return -1
        
        ans = min(money // 7, children)
        
        money -= ans * 7
        children -= ans
        
        if children == 0 and money > 0:
            return ans - 1
        
        if children == 1 and money == 3:
            return ans - 1
        
        return ans