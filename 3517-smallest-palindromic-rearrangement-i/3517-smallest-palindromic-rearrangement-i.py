class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        le = len(s)
        store = []
        
        if le <= 3:
            return s
        if le % 2 == 0:
            
            for i in range(le//2):
                store.append(s[i])
              
            store.sort()
            stor = "".join(store)

            return stor + stor[::-1]
        elif le % 2 != 0:
            for i in range(le//2):
                store.append(s[i])
            store.sort()    
            stor = "".join(store)    
            return stor + s[le//2] + stor[::-1]