# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree_height(self, node):
        if node is None:
            return 0
        left = self.tree_height(node.left)
        right = self.tree_height(node.right)
        return max(left, right) + 1
    def get_nodes_level(self, root, level):
        if root is None:
            return []
        if level == 1:
            return [root.val]
        return self.get_nodes_level(root.left, level - 1) + self.get_nodes_level(root.right, level - 1)
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # perform level-order traversal and append to list
        elements = []
        for level in range(1, self.tree_height(root) + 1):
            elements.extend(self.get_nodes_level(root, level))
        elements.sort()
        root = TreeNode()
        parent = root
        for i in range(len(elements)):
            parent.val = elements[i]
            if i != len(elements) - 1:
                parent.right = TreeNode()
                parent = parent.right
        return root