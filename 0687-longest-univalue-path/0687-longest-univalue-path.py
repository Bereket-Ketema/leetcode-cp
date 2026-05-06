# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root):
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            left = right = 0
            
            if node.left and node.left.val == node.val:
                left = l+1
            if node.right and node.right.val == node.val:
                right = r+1
            
            self.ans = max(self.ans,left+right)
            return max(left,right)
        
        dfs(root)
        return self.ans