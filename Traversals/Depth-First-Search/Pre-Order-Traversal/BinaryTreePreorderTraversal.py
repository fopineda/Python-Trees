# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        self.actualPreOrderTraversal(root, nodes)
        return nodes
        
        
    def actualPreOrderTraversal(self, root, nodes):
        if not root:
            return
        nodes.append(root.val)
        self.actualPreOrderTraversal(root.left, nodes)
        self.actualPreOrderTraversal(root.right, nodes)