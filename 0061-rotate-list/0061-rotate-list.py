class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Make it circular
        tail.next = head
        
        # Find new tail: (length - k % length - 1) steps
        k %= length
        steps = length - k - 1
        
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next
        
        # New head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head