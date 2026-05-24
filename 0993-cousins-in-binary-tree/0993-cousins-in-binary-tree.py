from collections import deque

class Solution:
    def isCousins(self, root, x, y):
        q = deque([(root, None)])
        
        while q:
            level = {}
            
            for _ in range(len(q)):
                node, parent = q.popleft()
                
                if node.val == x:
                    level[x] = parent
                
                if node.val == y:
                    level[y] = parent
                
                if node.left:
                    q.append((node.left, node))
                
                if node.right:
                    q.append((node.right, node))
            
            if x in level and y in level:
                return level[x] != level[y]
            
            if x in level or y in level:
                return False
        
        return False