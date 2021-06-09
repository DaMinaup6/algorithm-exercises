# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_not_same_position_chars_counter = defaultdict(int)
        guess_not_same_position_chars_counter  = defaultdict(int)
        same_position_count = 0
        for index in range(len(secret)):
            if secret[index] == guess[index]:
                same_position_count += 1
            else:
                secret_not_same_position_chars_counter[secret[index]] += 1
                guess_not_same_position_chars_counter[guess[index]]   += 1

        not_same_position_count = 0
        for char in guess_not_same_position_chars_counter:
            not_same_position_count += min(secret_not_same_position_chars_counter[char], guess_not_same_position_chars_counter[char])
        return "".join([str(same_position_count), "A", str(not_same_position_count), "B"])
