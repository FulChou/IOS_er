# 2020.04.13: 凌晨做的：
# 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def minDiffInBST(self, root: TreeNode) -> int:
        '''bst的中序遍历，是有顺序的：
        如果在函数中赋值时想让解释器把b当成全局变量，要使用global声明
        global min_diff, pre
        '''
        # def get_min(root,min_diff,pre):
        #     if root:
        #         min_diff,pre = get_min(root.left, min_diff, pre)
        #         min_diff = min(min_diff, root.val - pre)
        #         # print(root.val,pre)
        #         pre = root.val
        #         min_diff, pre = get_min(root.right, min_diff, pre)
        #     return min_diff, pre
        # min_diff = float('inf')
        # pre = -float('inf')
        # return get_min(root,min_diff, pre)[0]
        # 使用类变量，减少参数传递：
        self.min_diff = float('inf')
        self.pre = - float('inf')
        def get_min(root):
            if root:
                get_min(root.left)
                self.min_diff = min(self.min_diff, root.val - self.pre)
                self.pre = root.val
                get_min(root.right)
            return
        get_min(root)
        return self.min_diff