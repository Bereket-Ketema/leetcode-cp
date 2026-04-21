class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        store = [1]
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                store.append(i)
                if i != num // i:
                    store.append(num // i)

        return sum(store) == num