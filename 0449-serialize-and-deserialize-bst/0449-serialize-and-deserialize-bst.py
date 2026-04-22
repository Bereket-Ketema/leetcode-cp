class Codec:

    def serialize(self, root):
        vals = []
        
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        vals = list(map(int, data.split()))
        
        def build(lower, upper):
            if vals and lower < vals[0] < upper:
                val = vals.pop(0)
                node = TreeNode(val)
                node.left = build(lower, val)
                node.right = build(val, upper)
                return node
        
        return build(float('-inf'), float('inf'))