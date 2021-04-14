# -----------------------------------------
# My Solution
#
# Time  Complexity: O(tm) ~ O(t * 26^d)
# Space Complexity: O(tm)
# -----------------------------------------
# m := max length of word, t := total number of calls, d := max number of dots in one word
from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word  = False

class WordDictionary:

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]
        current_node.is_word = True


    def search(self, word: str) -> bool:
        def search_from_node(curr_node, start_index):
            for index in range(start_index, len(word)):
                char = word[index]
                # if char == '.', replace it with possible candidate and search
                if char == '.':
                    for candidate in curr_node.children:
                        if search_from_node(curr_node.children[candidate], index + 1):
                            return True
                    return False
                # if char != '.', just check if it exists in current node
                if char not in curr_node.children:
                    return False
                curr_node = curr_node.children[char]
            return curr_node.is_word

        return search_from_node(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
