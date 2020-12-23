'''
Author: Ful Chou
Date: 2020-11-11 12:03:18
LastEditors: Ful Chou
LastEditTime: 2020-12-23 11:49:59
FilePath: /leetcode/house_robber3.py
Description: What this document does
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """337 11.11日 9:30-12:00 leecode  [链接](https://leetcode-cn.com/problems/house-robber-iii/)
    12.23日 第二次做很快，不到半小时
    """
    def rob(self, root: TreeNode) -> int:
        pass
        # ### 这法子，最后一个样例通过不了, 这应该算递归的方法。
        # ### 很可能是因为python的原因。。。
        # dp_table = {}
        # if root == None:
        #     return 0
        # if root in dp_table.keys():
        #     print(root)
        #     return dp_table[root]
        # not_do = self.rob(root.left) + self.rob(root.right)
        # do = root.val
        # if root.left:
        #         do += self.rob(root.left.left) + self.rob(root.left.right)
        # if root.right:
        #         do += self.rob(root.right.left) + self.rob(root.right.right)
        # res = max(not_do, do)
        # dp_table[root] = res
        # return res
    def rob(self, root: TreeNode) -> int:
            '''
            逻辑含义：
            val_node = max(node_thief, node_thief_not)
            node_thief = self.val + self.left not +self.right not
            node_thief_not =  self.right + self.left
            '''
            def money(root):
                if not root:
                    return 0, 0
                left_thief, left_thief_not = money(root.left)
                right_thief, right_thief_not = money(root.right)
                node_thief = root.val + left_thief_not + right_thief_not
                node_thief_not =  max(left_thief, left_thief_not) + max(right_thief, right_thief_not)
                return node_thief, node_thief_not
            return max(money(root))

