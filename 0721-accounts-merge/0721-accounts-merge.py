from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        email_to_name = {}
        
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                parent.setdefault(email, email)
                email_to_name[email] = name
                union(acc[1], email)
        
        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)
        
        return [[email_to_name[k]] + sorted(v) for k, v in groups.items()]