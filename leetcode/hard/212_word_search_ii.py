# -----------------------------------------
# My Solution
#
# Time  Complexity: O(4^w + len(words) * w)
# Space Complexity: O(mn + len(words) * w)
# -----------------------------------------
# m := len(board), n := len(board[0]), w := max(words[i])
from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word  = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.visited_positions = set()
        self.found_words = set()
        self.trie = Trie()

        for word in words:
            self.trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.trie.root.children:
                    self.visited_positions.add((i, j))
                    self.search_from(self.trie.root.children[board[i][j]], board[i][j], i, j)
                    self.visited_positions.remove((i, j))

        return self.found_words

    def search_from(self, curr_node, curr_word, i, j):
        if curr_node.is_word:
            self.found_words.add(curr_word)

        if self.position_valid(i - 1, j) and self.board[i - 1][j] in curr_node.children:
            self.visited_positions.add((i - 1, j))
            self.search_from(curr_node.children[self.board[i - 1][j]], curr_word + self.board[i - 1][j], i - 1, j)
            self.visited_positions.remove((i - 1, j))

        if self.position_valid(i, j - 1) and self.board[i][j - 1] in curr_node.children:
            self.visited_positions.add((i, j - 1))
            self.search_from(curr_node.children[self.board[i][j - 1]], curr_word + self.board[i][j - 1], i, j - 1)
            self.visited_positions.remove((i, j - 1))

        if self.position_valid(i + 1, j) and self.board[i + 1][j] in curr_node.children:
            self.visited_positions.add((i + 1, j))
            self.search_from(curr_node.children[self.board[i + 1][j]], curr_word + self.board[i + 1][j], i + 1, j)
            self.visited_positions.remove((i + 1, j))

        if self.position_valid(i, j + 1) and self.board[i][j + 1] in curr_node.children:
            self.visited_positions.add((i, j + 1))
            self.search_from(curr_node.children[self.board[i][j + 1]], curr_word + self.board[i][j + 1], i, j + 1)
            self.visited_positions.remove((i, j + 1))

    def position_valid(self, i, j):
        return 0 <= i < len(self.board) and 0 <= j < len(self.board[0]) and (i, j) not in self.visited_positions

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O()
# Space Complexity: O(mn + len(words) * w)
# -----------------------------------------
# m := len(board), n := len(board[0]), w := max(words[i])
# Ref: https://blog.csdn.net/qq_31494411/article/details/52884470
from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word  = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def delete(self, word):
        current = self.root
        node_letter_stack = []

        for letter in word:
            if letter not in current.children:
                return
            node_letter_stack.append([current, letter])
            current = current.children[letter]
        if not current.is_word or len(current.children) > 0:
            return

        while len(node_letter_stack) > 0:
            node, letter = node_letter_stack.pop()
            del node.children[letter]

            if len(node.children) > 0 or node.is_word:
                break

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.visited_positions = set()
        self.found_words = set()
        self.trie = Trie()

        for word in words:
            self.trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.trie.root.children:
                    self.visited_positions.add((i, j))
                    self.search_from(self.trie.root.children[board[i][j]], board[i][j], i, j)
                    self.visited_positions.remove((i, j))

        return self.found_words

    def search_from(self, curr_node, curr_word, i, j):
        if curr_node.is_word:
            self.found_words.add(curr_word)
            self.trie.delete(curr_word)

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if self.position_valid(i + di, j + dj) and self.board[i + di][j + dj] in curr_node.children:
                self.visited_positions.add((i + di, j + dj))
                self.search_from(curr_node.children[self.board[i + di][j + dj]], curr_word + self.board[i + di][j + dj], i + di, j + dj)
                self.visited_positions.remove((i + di, j + dj))

    def position_valid(self, i, j):
        return 0 <= i < len(self.board) and 0 <= j < len(self.board[0]) and (i, j) not in self.visited_positions
