from typing import List,Set
import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        q = queue.Queue()
        # visit = set() 二叉树没有必要
        q.put(root)
        depth = 1
        if root == None : return 0
        while(not q.empty()):
            size = q.qsize()
            for i in range(0,size):
                node = q.get()
                #visit.add(node) # 避免重复放入 已经遍历过的node 二叉树的话，这个visit没有必要：
                if not node.left  and not node.right:
                    return depth
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            depth += 1
        return depth

    def minDepth(self, root: TreeNode) -> int:
        if not root: # 根节点本身不存在
            return 0
        if root.left and not root.right: #只有左节点
            return 1+self.minDepth(root.left)
        if root.right and not root.left: # 只有右节点
            return 1+self.minDepth(root.right)
        if not root.left and not root.right: #左右节点都没有
            return 1
        return 1+min(self.minDepth(root.left),self.minDepth(root.right)) #左右节点都有


if __name__ == "__main__":
    pass
    a = queue.Queue()
    a.put(2)
    a.put(2)
    a.put(3)
    while not a.empty():
        print(a.get())
    
    print(a.qsize())


