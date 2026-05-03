class Solution:
    def checkPalindromeFormation(self, a, b):
        def check(x,y):
            i,j=0,len(x)-1
            
            while i<j and x[i]==y[j]:
                i+=1
                j-=1
            
            s=x[i:j+1]
            t=y[i:j+1]
            return s==s[::-1] or t==t[::-1]
        
        return check(a,b) or check(b,a)