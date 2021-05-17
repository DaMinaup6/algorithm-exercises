# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
import functools
import collections

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_info = []
        for word in words:
            words_info.append((len(word), collections.Counter(word), word))
        words_info = sorted(words_info, key=lambda info: info[0])

        chain_mapping = collections.defaultdict(list)
        for curr_index, word_info in enumerate(words_info):
            curr_info = words_info[curr_index]
            for next_index in range(curr_index + 1, len(words_info)):
                next_info = words_info[next_index]
                if next_info[0] - curr_info[0] == 1 and len(next_info[1] - curr_info[1]) == 1 and len(curr_info[1] - next_info[1]) == 0:
                    curr_pointer, next_pointer = 0, 0
                    while curr_pointer < len(curr_info[2]) and next_pointer < len(next_info[2]):
                        while next_pointer < len(next_info[2]) and next_info[2][next_pointer] != curr_info[2][curr_pointer]:
                            next_pointer += 1
                        curr_pointer += 1
                        next_pointer += 1
                    if next_pointer - curr_pointer in [0, 1]:
                        chain_mapping[curr_info[2]].append(next_info[2])

        @functools.lru_cache(None)
        def dfs(curr_word, layer):
            max_layer = layer
            for next_word in chain_mapping[curr_word]:
                max_layer = max(max_layer, dfs(next_word, layer + 1))
            return max_layer
        return max([dfs(word, 1) for word in words])

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
import collections

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_lengths = set()
        word_chain_dict = collections.defaultdict(int)
        length_words_dict = collections.defaultdict(list)
        for word in words:
            word_lengths.add(len(word))
            word_chain_dict[word] = 1
            length_words_dict[len(word)].append((word, collections.Counter(word)))

        def is_successor(word, candidate):
            word_pointer, candidate_pointer = 0, 0
            while word_pointer < len(word) and candidate_pointer < len(candidate):
                while candidate_pointer < len(candidate) and candidate[candidate_pointer] != word[word_pointer]:
                    candidate_pointer += 1
                word_pointer += 1
                candidate_pointer += 1
            return candidate_pointer - word_pointer in [0, 1]

        max_chain = 1
        word_lengths = sorted(list(word_lengths))
        for index in range(len(word_lengths) - 1):
            if word_lengths[index + 1] - word_lengths[index] == 1:
                for word, word_char_count in length_words_dict[word_lengths[index + 1]]:
                    word_predecessor = None
                    for predecessor, predecessor_char_count in length_words_dict[word_lengths[index]]:
                        if len(predecessor_char_count - word_char_count) == 0 and len(word_char_count - predecessor_char_count) == 1 and is_successor(predecessor, word):
                            word_chain_dict[word] = max(word_chain_dict[word], word_chain_dict[predecessor] + 1)
                            max_chain = max(max_chain, word_chain_dict[word])
        return max_chain

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(mn + nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# m := max(len(word) for word in words) n := len(words)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        words_chain = {}
        longest_chain = 1
        for word in words:
            words_chain[word] = 1
            for index in range(len(word)):
                predecessor = word[:index] + word[(index + 1):]
                if predecessor in words_chain:
                    words_chain[word] = max(words_chain[word], words_chain[predecessor] + 1)
                    longest_chain = max(longest_chain, words_chain[word])
        return longest_chain
