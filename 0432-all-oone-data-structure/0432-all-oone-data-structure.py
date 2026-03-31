class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.key_map = {}   # key -> node

    def _add_node(self, new_node, prev_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.key_map:
            curr = self.key_map[key]
            next_node = curr.next
            
            if next_node == self.tail or next_node.count != curr.count + 1:
                new_node = Node(curr.count + 1)
                self._add_node(new_node, curr)
            else:
                new_node = next_node
            
            new_node.keys.add(key)
            self.key_map[key] = new_node
            
            curr.keys.remove(key)
            if not curr.keys:
                self._remove_node(curr)
        else:
            if self.head.next == self.tail or self.head.next.count != 1:
                new_node = Node(1)
                self._add_node(new_node, self.head)
            else:
                new_node = self.head.next
            
            new_node.keys.add(key)
            self.key_map[key] = new_node

    def dec(self, key: str) -> None:
        if key not in self.key_map:
            return
        
        curr = self.key_map[key]
        
        if curr.count == 1:
            del self.key_map[key]
        else:
            prev_node = curr.prev
            
            if prev_node == self.head or prev_node.count != curr.count - 1:
                new_node = Node(curr.count - 1)
                self._add_node(new_node, curr.prev)
            else:
                new_node = prev_node
            
            new_node.keys.add(key)
            self.key_map[key] = new_node
        
        curr.keys.remove(key)
        if not curr.keys:
            self._remove_node(curr)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))