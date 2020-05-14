# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        self.actualpostorderTraversal(root, nodes)
        return nodes
        
        
    def actualpostorderTraversal(self, root, nodes):
        if not root:
            return
        self.actualpostorderTraversal(root.left, nodes)
        self.actualpostorderTraversal(root.right, nodes)
        nodes.append(root.val)