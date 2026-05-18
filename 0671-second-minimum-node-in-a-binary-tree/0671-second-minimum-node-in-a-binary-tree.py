# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root):
        self.ans = float('inf')
        mn = root.val
        
        def dfs(node):
            if not node:
                return
            
            if mn < node.val < self.ans:
                self.ans = node.val
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.ans if self.ans != float('inf') else -1