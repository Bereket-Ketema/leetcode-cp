class Solution:
    def evaluateTree(self, root):
        if root.val == 0:
            return False

        if root.val == 1:
            return True

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:
            return left or right

        return left and right