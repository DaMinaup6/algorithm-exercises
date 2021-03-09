# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=lsQTYlCiU6c
class Solution:
    def largestRectangleArea(self, heights):
        h_stack = [] # stack of heights
        p_stack = [] # stack of positions
        heights.append(0) # force to empty stack before while loop ends

        max_area = 0
        for index in range(len(heights)):
            last_position = len(heights) + 1

            while len(h_stack) > 0 and h_stack[-1] > heights[index]:
                last_position = p_stack[-1]
                current_area  = (index - p_stack.pop()) * h_stack.pop()
                max_area = max(max_area, current_area)

            if len(h_stack) == 0 or h_stack[-1] < heights[index]:
                h_stack.append(heights[index])
                p_stack.append(min(last_position, index))

        return max_area
