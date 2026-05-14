# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2):
        def leaves(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return leaves(root.left) + leaves(root.right)
        
        return leaves(root1) == leaves(root2)