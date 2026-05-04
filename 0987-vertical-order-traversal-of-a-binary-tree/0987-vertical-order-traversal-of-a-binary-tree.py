# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root):
        cols = defaultdict(list)
        
        def dfs(node, r, c):
            if not node:
                return
            cols[c].append((r, node.val))
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
        
        dfs(root,0,0)
        
        res=[]
        for c in sorted(cols):
            cols[c].sort()
            res.append([v for _,v in cols[c]])
        
        return res