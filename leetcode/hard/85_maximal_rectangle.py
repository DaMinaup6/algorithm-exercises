# -----------------------------------------
# My Solution
#
# Time  Complexity: O((mn)^2)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
class Solution:
    def maximalRectangle(self, matrix):
        def is_one(i, j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == '1'

        def calc_down_rectangle_area(i, j): # get the farest down position and scan from left to right
            end_i = i + 1
            end_j = j
            while is_one(end_i + 1, j):
                end_i += 1
            while all(is_one(tmp_i, j - 1) for tmp_i in range(i, end_i + 1)):
                j -= 1
            while all(is_one(tmp_i, end_j + 1) for tmp_i in range(i, end_i + 1)):
                end_j += 1

            return (end_i - i + 1) * (end_j - j + 1)

        def calc_right_rectangle_area(i, j): # get the farest right position and scan from top to bottom
            end_i = i
            end_j = j + 1
            while is_one(i, end_j + 1):
                end_j += 1
            while all(is_one(i - 1, tmp_j) for tmp_j in range(j, end_j + 1)):
                i -= 1
            while all(is_one(end_i + 1, tmp_j) for tmp_j in range(j, end_j + 1)):
                end_i += 1

            return (end_i - i + 1) * (end_j - j + 1)

        def max_rectangle_area_from(i, j):
            if not is_one(i, j):
                return 0

            down_rectangle_area  = 1
            right_rectangle_area = 1
            if is_one(i + 1, j):
                down_rectangle_area = calc_down_rectangle_area(i, j)
            if is_one(i, j + 1):
                right_rectangle_area = calc_right_rectangle_area(i, j)

            return max(right_rectangle_area, down_rectangle_area)

        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_area = max(max_area, max_rectangle_area_from(i, j))

        return max_area

# -----------------------------------------
# Calculate largest rectangle in histogram
#
# Time  Complexity: O(mn)
# Space Complexity: O(n)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
class Solution:
    def largest_rectangle_area(self, heights): # from problem 84
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

    def maximalRectangle(self, matrix):
        if matrix is None or len(matrix) == 0:
            return 0

        # e.g.
        # [
        #   [1, 0, 0, 1, 1, 1],
        #   [1, 0, 1, 1, 0, 1],
        # ]
        # this equals to find largest rectangle in two histograms
        # histogram 1: [1, 0, 0, 1, 1, 1]
        # histogram 2: [2, 0, 1, 2, 0, 1]
        max_area = 0
        heights  = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largest_rectangle_area(heights))

        return max_area
