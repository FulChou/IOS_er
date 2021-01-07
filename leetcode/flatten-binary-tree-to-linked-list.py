'''
Author: Ful Chou
Date: 2021-01-07 11:38:03
LastEditors: Ful Chou
LastEditTime: 2021-01-07 11:38:33
FilePath: /leetcode/flatten-binary-tree-to-linked-list.py
Description: What this document does
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        写递归的思路：
        不要进入递归函数里面去想，要想好当前函数是做什么事情，然后假定 递归函数 已经按照你当前定义的函数做好了，
        写好当前定义就好了，递归会自己执行好
        """
        if root == None:
            return
        if root.left: # 以为少一层堆栈可以节约内容，结果看没太大的帮助
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        child_right = root.right
        root.right = root.left
        root.left = None # 原来的左子树 要记得清零
        p = root 
        while p.right:
            p = p.right
        p.right = child_right