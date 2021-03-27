# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(n)
# -----------------------------------------
# m := len(beginWord) == len(endWord) == len(wordList[i]), n := len(wordList)
# Ref:
# a) https://www.youtube.com/watch?v=hB_nYXFtwP0
# b) https://blog.csdn.net/fuxuemingzhu/article/details/82903681
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list_set = set(wordList)
        if endWord not in word_list_set:
            return 0
        
        queue = deque([beginWord])
        level = 0
        while len(queue) > 0:
            queue_size = len(queue)
            for _ in range(queue_size):
                word = queue.popleft()
                if word == endWord:
                    return level + 1

                word_array = list(word)
                for index in range(len(word_array)):
                    tmp_char = word_array[index]
                    for char_idx in range(ord('a'), ord('z') + 1):
                        char = chr(char_idx)
                        if char == tmp_char:
                            continue

                        word_array[index] = chr(char_idx)
                        new_word = ''.join(word_array)
                        if new_word in word_list_set:
                            queue.append(new_word)
                            word_list_set.remove(new_word)
                    word_array[index] = tmp_char
            level += 1

        return 0
