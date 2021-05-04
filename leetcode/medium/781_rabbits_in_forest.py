# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
import collections
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer_count_dict = collections.defaultdict(int)
        for answer in answers:
            answer_count_dict[answer] += 1

        min_rabbits_num = 0
        for answer in answer_count_dict:
            answer_count = answer_count_dict[answer]
            min_rabbits_num += math.ceil(answer_count / (answer + 1)) * (answer + 1)
        return min_rabbits_num
