# -----------------------------------------
# My Solution
#
# Time  Complexity: O(min(m, n))
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(sentence1), n := len(sentence2)
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentences_1 = sentence1.split(' ')
        sentences_2 = sentence2.split(' ')
        if len(sentences_2) > len(sentences_1): # set sentences_2 to be the shorter one for convenience
            sentences_1, sentences_2 = sentences_2, sentences_1

        # Case 1: sentences_1 == ['a', 'b', 'c', 'd'], sentences_2 == ['a', 'b']
        last_forward_matched_index = -1
        for index in range(len(sentences_2)):
            if sentences_1[index] == sentences_2[index]:
                last_forward_matched_index = index
            else:
                break
        if last_forward_matched_index == len(sentences_2) - 1:
            return True
        
        # Case 2: sentences_1 == ['a', 'b', 'c', 'd'], sentences_2 == ['c', 'd']
        last_backward_matched_index = len(sentences_2)
        for index in range(-1, -len(sentences_2) - 1, -1):
            if sentences_1[index] == sentences_2[index]:
                last_backward_matched_index = index + len(sentences_2)
            else:
                break
        if last_backward_matched_index == 0:
            return True

        # Case 3: sentences_1 == ['a', 'b', 'c', 'd'], sentences_2 == ['a', 'c', 'd']
        #         check last matched index forward and backward see if they connect
        return last_backward_matched_index - last_forward_matched_index == 1
