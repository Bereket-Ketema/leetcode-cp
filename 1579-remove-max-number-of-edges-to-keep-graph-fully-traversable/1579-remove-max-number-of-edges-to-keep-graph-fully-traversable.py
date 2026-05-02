class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        class UF:
            def __init__(self,n):
                self.p=list(range(n+1))
                self.c=n
            
            def find(self,x):
                if self.p[x]!=x:
                    self.p[x]=self.find(self.p[x])
                return self.p[x]
            
            def union(self,a,b):
                pa,pb=self.find(a),self.find(b)
                if pa==pb:
                    return False
                self.p[pa]=pb
                self.c-=1
                return True
        
        alice=UF(n)
        bob=UF(n)
        used=0
        
        for t,u,v in edges:
            if t==3:
                a=alice.union(u,v)
                b=bob.union(u,v)
                if a or b:
                    used+=1
        
        for t,u,v in edges:
            if t==1 and alice.union(u,v):
                used+=1
            elif t==2 and bob.union(u,v):
                used+=1
        
        if alice.c!=1 or bob.c!=1:
            return -1
        
        return len(edges)-used