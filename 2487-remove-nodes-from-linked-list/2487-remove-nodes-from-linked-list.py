# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and stack[-1] < head.val:
                stack.pop()
            stack.append(head.val)
            head = head.next
        
        dummy = ListNode()
        head = dummy
        for num in stack:
            new_node = ListNode(num)
            dummy.next = new_node
            dummy = dummy.next

        return head.next