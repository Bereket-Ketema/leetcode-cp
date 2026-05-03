class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        edgeList.sort(key=lambda x:x[2])
        q = sorted([(l,u,v,i) for i,(u,v,l) in enumerate(queries)])
        
        parent=list(range(n))
        
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(a,b):
            pa,pb=find(a),find(b)
            if pa!=pb:
                parent[pa]=pb
        
        ans=[False]*len(queries)
        j=0
        
        for limit,u,v,i in q:
            while j<len(edgeList) and edgeList[j][2]<limit:
                union(edgeList[j][0],edgeList[j][1])
                j+=1
            
            ans[i]=(find(u)==find(v))
        
        return ans