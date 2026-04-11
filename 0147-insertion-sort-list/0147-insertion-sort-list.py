class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        
        while head:
            prev = dummy
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            
            next_node = head.next
            head.next = prev.next
            prev.next = head
            head = next_node
        
        return dummy.next