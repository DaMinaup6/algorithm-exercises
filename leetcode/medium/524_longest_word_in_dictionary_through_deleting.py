# -----------------------------------------
# My Solution: Binary Search
#
# Time  Complexity: O(dm * log(n))
# Space Complexity: O(n)
# -----------------------------------------
# d := len(dictionary), m := max(len(word) for word in dictionary), n := len(s)
import collections
import bisect

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        s_char_indexes = collections.defaultdict(list)
        for index, char in enumerate(s):
            s_char_indexes[char].append(index)

        longest_word = ""
        for word in dictionary:
            if len(word) < len(longest_word):
                continue

            word_valid = True
            prev_char_index = -1
            for char in word:
                if char not in s_char_indexes:
                    word_valid = False
                    break

                next_char_position = bisect.bisect_left(s_char_indexes[char], prev_char_index + 1)
                if next_char_position == len(s_char_indexes[char]):
                    word_valid = False
                    break
                else:
                    prev_char_index = s_char_indexes[char][next_char_position]

            if word_valid:
                if len(word) > len(longest_word):
                    longest_word = word
                elif len(word) == len(longest_word):
                    longest_word = sorted((longest_word, word))[0]
        return longest_word
