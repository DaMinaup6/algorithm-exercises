# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn * 4^t)
# Space Complexity: O(mn + t)
# -----------------------------------------
# m := len(board), n := len(board[0]), t := len(word)
#
# from collections import defaultdict
#
# def check_word(board, word, word_char_indexes, current_index, i, j, checked_positions):
#     if current_index == len(word) - 1:
#         return True
#
#     next_positions = []
#     if i > 0:
#         next_positions.append([i - 1, j])
#     if j > 0:
#         next_positions.append([i, j - 1])
#     if i < len(board) - 1:
#         next_positions.append([i + 1, j])
#     if j < len(board[0]) - 1:
#         next_positions.append([i, j + 1])
#
#     for next_position in next_positions:
#         if current_index + 1 not in word_char_indexes[board[next_position[0]][next_position[1]]]:
#             continue
#         if (next_position[0], next_position[1]) in checked_positions:
#             continue
#         new_checked_positions = set(list(checked_positions) + [(next_position[0], next_position[1])])
#         if not check_word(board, word, word_char_indexes, current_index + 1, next_position[0], next_position[1], new_checked_positions):
#             continue
#
#         return True        
#
#     return False
#
# class Solution:
#     def exist(self, board, word):
#         word_char_indexes = defaultdict(set)
#         for char_index, char in enumerate(word):
#             word_char_indexes[char].add(char_index)
#
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 matched_indexes = word_char_indexes[board[i][j]]
#                 if 0 in matched_indexes and check_word(board, word, word_char_indexes, 0, i, j, set([(i, j)])):
#                     return True
#
#         return False

# -----------------------------------------
# My Solution (simplified)
#
# Time  Complexity: O(mn * 4^t)
# Space Complexity: O(mn + t)
# -----------------------------------------
# m := len(board), n := len(board[0]), t := len(word)
class Solution:
    def exist(self, board, word):
        def search_from(i, j, cursor):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[cursor]:
                return False
            if cursor == len(word) - 1:
                return True

            letter_cell = board[i][j]
            board[i][j] = ''
            if search_from(i + 1, j, cursor + 1):
                return True
            if search_from(i - 1, j, cursor + 1):
                return True
            if search_from(i, j + 1, cursor + 1):
                return True
            if search_from(i, j - 1, cursor + 1):
                return True
            board[i][j] = letter_cell

            return False

        return any(search_from(i, j, 0) for i in range(len(board)) for j in range(len(board[0])))
