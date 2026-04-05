# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Ignore negative paths
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # Path through current node
            current = node.val + left + right
            
            # Update global max
            self.max_sum = max(self.max_sum, current)
            
            # Return max path extending upward
            return node.val + max(left, right)
        
        dfs(root)
        return self.max_sum