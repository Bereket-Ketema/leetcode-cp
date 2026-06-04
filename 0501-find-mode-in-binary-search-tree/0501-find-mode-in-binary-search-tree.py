# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter

class Solution:
    def findMode(self, root):
        cnt = Counter()

        def dfs(node):
            if not node:
                return

            cnt[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        mx = max(cnt.values())

        return [x for x, f in cnt.items() if f == mx]