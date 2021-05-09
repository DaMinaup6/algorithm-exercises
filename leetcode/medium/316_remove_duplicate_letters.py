# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref:
# a) https://blog.csdn.net/fuxuemingzhu/article/details/86063211
# b) https://www.youtube.com/watch?v=-zmul9EyKng
import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_counter = collections.Counter(s)
        char_placed  = collections.defaultdict(bool)
        char_stack   = []
        for char in s:
            char_counter[char] -= 1
            if char_placed[char]:
                continue

            while len(char_stack) > 0 and char_counter[char_stack[-1]] > 0 and char_stack[-1] > char:
                char_placed[char_stack[-1]] = False
                char_stack.pop()
            char_placed[char] = True
            char_stack.append(char)

        return "".join(char_stack)
