class Solution:
    def binaryGap(self, n: int) -> int:
        a = bin(n)[2:]
        if a.count('1') < 2:
            return 0

        first, second = 0, 0
        Flag = False
        store = 0
        for i, v in enumerate(a):
            if v == '1':
                if Flag:
                    second = i
                    store = max(store, second - first)
                    first = second
                else:
                    first = i
                    Flag = True
        return store
        
        
