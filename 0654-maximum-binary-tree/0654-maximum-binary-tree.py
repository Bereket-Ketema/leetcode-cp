# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        
        def build(left, right):
            if left > right:
                return None

            max_index = left
            for i in range(left, right + 1):
                if nums[i] > nums[max_index]:
                    max_index = i

            root = TreeNode(nums[max_index])

            root.left = build(left, max_index - 1)
            root.right = build(max_index + 1, right)
            
            return root
        
        return build(0, len(nums) - 1)