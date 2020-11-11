class Solution:
    """337 11.11日 9:30-12:00 leecode  [链接](https://leetcode-cn.com/problems/house-robber-iii/)
    """
    def rob(self, root: TreeNode) -> int:
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
        def _rob(root):
            if not root: return 0, 0 # 0 不偷，1 偷
            left = _rob(root.left)
            right = _rob(root.right)
            return root.val + left[1] + right[1], max(left) + max(right)
        
        return max(_rob(root))