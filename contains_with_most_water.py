def maxArea(height):
    if len(height) <= 1:
        return 0

    left_cursor  = 0
    right_cursor = len(height) - 1
    max_area = 0

    while left_cursor != right_cursor:
        area = min(height[left_cursor], height[right_cursor]) * (right_cursor - left_cursor)
        if area > max_area:
            max_area = area

        if height[left_cursor] < height[right_cursor]:
            left_cursor += 1
        else:
            right_cursor -= 1

    return max_area

print(f"maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]): correct: {maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49}")
