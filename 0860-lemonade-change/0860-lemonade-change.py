class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store = defaultdict(int)
        for cent in bills:
            store[cent] += 1
            if cent == 10:
                if 5 in store and store[5] > 0:
                    store[5] -= 1
                else:
                    return False
            elif cent == 20:
                if 10 in store and  store[10] > 0 and 5 in store and  store[5] > 0:
                        store[5] -= 1
                        store[10] -= 1
                elif 5 in store and store[5] >= 3:
                    store[5] -= 3
                else:
                    return False
        return True