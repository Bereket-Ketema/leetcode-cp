# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pathSum(self, root, targetSum):
        prefix = defaultdict(int)
        prefix[0] = 1
        self.count = 0

        def dfs(node, curr_sum):
            if not node:
                return
            
            curr_sum += node.val
            self.count += prefix[curr_sum - targetSum]
            prefix[curr_sum] += 1
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            prefix[curr_sum] -= 1

        dfs(root, 0)
        return self.count