# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(n + kp)
# -----------------------------------------
# m := len(beginWord) == len(endWord) == len(wordList[i]), n := len(wordList), k := number of paths, p := length of path
# Ref: https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/126.%20Word%20Ladder%20II.md
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words_set = set(wordList)
        if endWord not in words_set:
            return []

        words_set.add(beginWord)
        word_transform_dict, current_transform_set = {word: [] for word in words_set}, set([beginWord])
        while current_transform_set and endWord not in current_transform_set:
            for word in current_transform_set:
                words_set.remove(word)

            next_transform_set = set()
            for word in current_transform_set:
                for index in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:index] + char + word[(index + 1):]
                        if candidate in words_set:
                            word_transform_dict[candidate].append(word)
                            next_transform_set.add(candidate)
            current_transform_set = next_transform_set
        # if current_transform_set is empty after while loop means we couldn't reach endWord
        if len(current_transform_set) == 0:
            return []

        # here use backtrack because starts from endWord to beginWord would avoid many transformations that cannot reach endWord
        word_ladders = []
        def backtrack_word_ladders(word_ladder, word):
            if len(word_transform_dict[word]) == 0:
                word_ladders.append([word] + word_ladder)
            else:
                for prev_word in word_transform_dict[word]:
                    backtrack_word_ladders([word] + word_ladder, prev_word)
        backtrack_word_ladders([], endWord)

        return word_ladders
