# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn^2)
# Space Complexity: O(mn)
# -----------------------------------------
# m := max(len(word) for word in words), n := len(words)
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_char_sets = []
        for word in words:
            word_char_sets.append(set(word))

        max_product = 0
        for word_1_index in range(len(words) - 1):
            for word_2_index in range(word_1_index + 1, len(words)):
                if not any(char in word_char_sets[word_2_index] for char in word_char_sets[word_1_index]):
                    max_product = max(max_product, len(words[word_1_index]) * len(words[word_2_index]))
        return max_product

# -----------------------------------------
# Model Solution: Bit Manipulation
#
# Time  Complexity: O(mn + b^2)
# Space Complexity: O(b)
# -----------------------------------------
# m := max(len(word) for word in words), n := len(words), b := len(masks)
# Ref: https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/76970/Python-solution-beats-99.67
import collections

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # e.g. word == "ab", mask would be 3 (since "a" represents 1 and "b" represents 10 in binary respresentation)
        #      so mask_max_length_dict[3] == len(word)
        #      but if now word == "abb", it generates same mask but we should update the value to 3
        mask_max_length_dict = collections.defaultdict(int)
        for word in words:
            mask = 0
            for char in set(word):
                mask |= 1 << (ord(char) - ord('a'))
            mask_max_length_dict[mask] = max(mask_max_length_dict[mask], len(word))

        masks = list(mask_max_length_dict.keys())
        max_product = 0
        for index_1 in range(len(masks) - 1):
            for index_2 in range(index_1 + 1, len(masks)):
                mask_1, mask_2 = masks[index_1], masks[index_2]
                # if a & b == 0 then it means for each binary bit in a not same as in b
                if mask_1 & mask_2 == 0:
                    max_length_1 = mask_max_length_dict[mask_1]
                    max_length_2 = mask_max_length_dict[mask_2]
                    max_product  = max(max_product, max_length_1 * max_length_2)
        return max_product
