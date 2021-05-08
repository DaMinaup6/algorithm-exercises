# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nw + m)
# Space Complexity: O(nw + m)
# -----------------------------------------
# m := len(dictionary), n := len(sentence.split(" ")), r := max(len(root) for root in dictionary), w := max(len(word) for word in sentence.split(" "))
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots_set = set(dictionary)

        replaced_sentence = ""
        for word in sentence.split(" "):
            curr_str = ""
            for index in range(len(word)):
                curr_str += word[index]
                if curr_str in roots_set:
                    break

            if len(replaced_sentence) == 0:
                replaced_sentence += curr_str
            else:
                replaced_sentence += " " + curr_str

        return replaced_sentence

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nw + md)
# Space Complexity: O(nw + md)
# -----------------------------------------
# m := len(dictionary), n := len(sentence.split(" ")), r := max(len(root) for root in dictionary), w := max(len(word) for word in sentence.split(" "))
# Ref: https://leetcode.com/problems/replace-words/solution/
from collections import defaultdict

class Node:

    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word  = False


class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.children[char]
        current.is_word = True


    def get_root(self, word: str) -> str:
        current = self.root
        root = ""
        for char in word:
            if char not in current.children:
                break

            current = current.children[char]
            root += char
            if current.is_word:
                return root

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        replaced_words = []
        for word in sentence.split(" "):
            replaced_words.append(trie.get_root(word))

        return " ".join(replaced_words)
