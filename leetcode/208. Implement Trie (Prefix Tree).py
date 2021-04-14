class Trie:
    '''  字典树，一次构建，多次查询：
    优化过程： 使用list 代替 dict， 理论上来说更加节约内存！
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sub_tree = [None] * 26 # 用list的话， indx ： ord(s) - ord('a'), 实际运行来看使用list 并没有优化到内存，可能和题目的测试用例有关，用例少的话，确实使用 dict 还划算一些
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.sub_tree[idx] == None:
                node.sub_tree[idx] = Trie()
            node = node.sub_tree[idx]
        node.isEnd = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.sub_tree[idx] != None:
                node = node.sub_tree[idx]
            else: return False
        return node.isEnd


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if node.sub_tree[idx] != None:
                node = node.sub_tree[idx]
            else: return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)