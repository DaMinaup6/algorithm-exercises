# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(n)
# -----------------------------------------
# m := len(beginWord) == len(endWord) == len(wordList[i]), n := len(wordList)
# Ref: https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/126.%20Word%20Ladder%20II.md
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def backtrack(path, word):
            if len(trace[word]) == 0:
                result.append([word] + path)
            else:
                for prev in trace[word]:
                    backtrack([word] + path, prev)

        word_set = set(wordList)
        if endWord not in word_set:
            return []

        word_set.add(beginWord)
        result, trace, current_set = [], {word: [] for word in word_set}, set([beginWord])
        while current_set and endWord not in current_set:
            for word in current_set:
                word_set.remove(word)

            new_set = set()
            for word in current_set:
                for index in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:index] + char + word[(index + 1):]
                        if candidate in word_set:
                            trace[candidate].append(word)
                            new_set.add(candidate)
            current_set = new_set

        if len(current_set) > 0:
            backtrack([], endWord)
        return result
