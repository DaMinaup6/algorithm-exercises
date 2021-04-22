# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=lsQTYlCiU6c
class Solution:
    def largestRectangleArea(self, heights):
        hight_start_index_stack = [] # stack of (height, start_index)
        heights.append(0) # force to empty stack before while loop ends

        max_area = 0
        for curr_index, curr_height in enumerate(heights):
            start_index = len(heights) + 1
            while len(hight_start_index_stack) > 0 and hight_start_index_stack[-1][0] > curr_height:
                prev_height, start_index = hight_start_index_stack.pop()
                max_area = max(max_area, (curr_index - start_index) * prev_height)

            if len(hight_start_index_stack) == 0 or hight_start_index_stack[-1][0] < curr_height:
                hight_start_index_stack.append((curr_height, min(start_index, curr_index)))

        return max_area
