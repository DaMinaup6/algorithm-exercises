# -----------------------------------------
# My Solution: Pointers
#
# Time  Complexity: O(mn + n)
# Space Complexity: O(n)
# -----------------------------------------
# m := len(s), n := len(words), w := max(words[i])
# Note: This solution leads to TLE
import collections
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_pointers = [0] * len(words)
        for char in s:
            for index, word in enumerate(words):
                if word_pointers[index] < len(word) and word[word_pointers[index]] == char:
                    word_pointers[index] += 1

        return sum(word_pointers[index] == len(word) for index, word in enumerate(words))

# -----------------------------------------
# My Solution: Hashmap + Binary Search
#
# Time  Complexity: O(nwlog(m) + m)
# Space Complexity: O(m)
# -----------------------------------------
# m := len(s), n := len(words), w := max(words[i])
import collections
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        s_char_indexes_dict = collections.defaultdict(list)
        for index, char in enumerate(s):
            s_char_indexes_dict[char].append(index)

        total_subsequences = 0
        for word in words:
            valid_subsequence = True
            prev_index = -1

            for char in word:
                if char not in s_char_indexes_dict:
                    valid_subsequence = False
                    break

                s_char_index = bisect.bisect_left(s_char_indexes_dict[char], prev_index + 1)
                if s_char_index == len(s_char_indexes_dict[char]):
                    valid_subsequence = False
                    break
                else:
                    prev_index = s_char_indexes_dict[char][s_char_index]

            if valid_subsequence:
                total_subsequences += 1

        return total_subsequences
