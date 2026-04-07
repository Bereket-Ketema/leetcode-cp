# Definition for a Node.
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

class Solution:
    def flatten(self, head):
        if not head:
            return head
        
        def dfs(node):
            curr = node
            last = node
            
            while curr:
                next_node = curr.next
                
                if curr.child:
                    child_last = dfs(curr.child)
                    
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None
                    
                    if next_node:
                        child_last.next = next_node
                        next_node.prev = child_last
                    
                    last = child_last
                else:
                    last = curr
                
                curr = next_node
            
            return last
        
        dfs(head)
        return head