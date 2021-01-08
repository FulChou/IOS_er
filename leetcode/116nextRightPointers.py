'''
Author: Ful Chou
Date: 2021-01-08 11:05:23
LastEditors: Ful Chou
LastEditTime: 2021-01-08 11:06:11
FilePath: /leetcode/116nextRightPointers.py
Description: What this document does
链接： https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # if root and root.left:
        #     self.connectTree(root.left,root.right)
        self.connectTree2(root)
        return root

    
    def connectTree(self,left,right): # 216ms
        if left == None:
            return
        else:
            left.next = right
            self.connectTree(left.left,left.right)
            self.connectTree(left.right,right.left)
            self.connectTree(right.left,right.right)
    
    def connectTree2(self,root): # 这种方法 快很多！
        if root:
            if root.left:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                self.connectTree2(root.left)
                self.connectTree2(root.right)
            else: return
        else: return