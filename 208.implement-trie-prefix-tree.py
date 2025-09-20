#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.content = []

    def insert(self, word: str) -> None:
        self.content.append(word)

    def search(self, word: str) -> bool:
        for content in self.content:
            if word == content:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for content in self.content:
            if content.startswith(prefix):
                return True
        return False
# class TrieNode:
#     __slots__ = ("children", "end")
#     def __init__(self):
#         self.children = {}
#         self.end = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         node = self.root
#         for ch in word:
#             node = node.children.setdefault(ch, TrieNode())
#         node.end = True

#     def search(self, word: str) -> bool:
#         node = self.root
#         for ch in word:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return node.end

#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for ch in prefix:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

