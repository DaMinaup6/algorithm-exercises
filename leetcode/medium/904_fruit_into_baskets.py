# -----------------------------------------
# My Solution: Two Pointers
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        max_amount_collect = 0

        left_pointer, right_pointer = 0, 0
        fruit_amount_collect = 0
        fruit_types_count = defaultdict(int)
        while right_pointer < len(tree):
            # find substring that contains only two types of fruit
            while right_pointer < len(tree) and (len(fruit_types_count) < 2 or tree[right_pointer] in fruit_types_count):
                fruit_amount_collect += 1
                fruit_types_count[tree[right_pointer]] += 1
                right_pointer += 1

            # update max_amount_collect
            max_amount_collect = max(max_amount_collect, fruit_amount_collect)

            # move left_pointer until there is only one type of fruit remains
            while left_pointer < right_pointer and len(fruit_types_count) == 2:
                fruit_amount_collect -= 1
                fruit_types_count[tree[left_pointer]] -= 1
                if fruit_types_count[tree[left_pointer]] == 0:
                    del fruit_types_count[tree[left_pointer]]
                left_pointer += 1

        return max_amount_collect
