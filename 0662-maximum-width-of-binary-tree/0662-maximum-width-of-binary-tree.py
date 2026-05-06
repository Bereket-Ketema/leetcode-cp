# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        q = deque([(root,0)])
        ans = 0
        
        while q:
            ans = max(ans, q[-1][1]-q[0][1]+1)
            
            for _ in range(len(q)):
                node,idx = q.popleft()
                
                if node.left:
                    q.append((node.left,2*idx))
                if node.right:
                    q.append((node.right,2*idx+1))
        
        return ans