class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root