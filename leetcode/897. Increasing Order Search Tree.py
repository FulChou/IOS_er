# 2021.04.25
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.head = TreeNode()
        self.temp = self.head
        def mid_first(root: TreeNode):
            if root == None:
                return 
            mid_first(root.left)
            # self.temp.right = TreeNode(root.val)
            # self.temp = self.temp.right
            self.temp.right = root #  方法二: 不需要新建 Node
            root.left = None
            self.temp = root
            mid_first(root.right)
        mid_first(root)
        return self.head.right