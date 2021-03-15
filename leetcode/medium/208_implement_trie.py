# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/79388432
from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.isword   = False

class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.children[char]
        current.isword = True


    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.isword


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
