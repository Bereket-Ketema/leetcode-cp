# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n):
        if n % 2 == 0:
            return []
        
        memo = {}
        
        def dfs(n):
            if n == 1:
                return [TreeNode(0)]
            if n in memo:
                return memo[n]
            
            res = []
            for left in range(1, n, 2):
                right = n - 1 - left
                for l in dfs(left):
                    for r in dfs(right):
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
            
            memo[n] = res
            return res
        
        return dfs(n)