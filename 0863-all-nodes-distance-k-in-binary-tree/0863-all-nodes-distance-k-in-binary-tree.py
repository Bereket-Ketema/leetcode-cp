# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, k):
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        
        def build(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build(node.left, node)
            build(node.right, node)
        
        build(root, None)
        
        q = deque([(target.val, 0)])
        visited = {target.val}
        res = []
        
        while q:
            node, dist = q.popleft()
            if dist == k:
                res.append(node)
            elif dist < k:
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, dist + 1))
        
        return res