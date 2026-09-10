# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0, 0
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            tot_sum = ls + rs + node.val
            tot_cnt = lc + rc + 1
            if tot_sum // tot_cnt == node.val:
                ans += 1
            return tot_sum, tot_cnt
        dfs(root)
        return ans