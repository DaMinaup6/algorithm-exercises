# -----------------------------------------
# O(n^2): My Solution
# -----------------------------------------
class Solution:
    def trap(self, height):
        if len(height) <= 2:
            return 0

        volume = 0
        cursor = 0
        while cursor < len(height) - 1:
            # Step 0: skip zero height and height lower than or equal to next height
            if height[cursor] == 0 or height[cursor + 1] >= height[cursor]:
                cursor += 1
                continue

            # Step 1: find bound for cursor
            bound_idx = cursor + 2
            if bound_idx >= len(height):
                break

            tmp_idx = bound_idx
            while tmp_idx < len(height):
                current_height = height[tmp_idx]
                if current_height > height[bound_idx]:
                    bound_idx = tmp_idx
                if current_height >= height[cursor]:
                    break
                tmp_idx += 1

            # Step 2: calculate rain water volume between range
            if height[bound_idx] == 0:
                break
            else:
                range_height = min(height[cursor], height[bound_idx])
                range_width  = (bound_idx - cursor - 1)
                range_area   = range_height * range_width
                for h in height[(cursor + 1):bound_idx]:
                    range_area -= min(range_height, h) * 1
                volume += range_area

                cursor = bound_idx

        return volume

processor = Solution()
print(f"processor.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6: {processor.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6}")
print(f"processor.trap([4, 2, 0, 3, 2, 5])                   == 9: {processor.trap([4, 2, 0, 3, 2, 5]) == 9}")
print(f"processor.trap([5, 4, 1, 2])                         == 1: {processor.trap([5, 4, 1, 2]) == 1}")
