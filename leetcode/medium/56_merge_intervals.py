# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(max(start_i))
# -----------------------------------------
class Solution:
    def merge(self, intervals):
        max_start = -1
        for interval in intervals:
            if interval[0] > max_start:
                max_start = interval[0]

        end_position_array = [None for _ in range(max_start + 1)]
        for interval in intervals:
            if end_position_array[interval[0]] is None:
                end_position_array[interval[0]] = interval[1]
            else:
                end_position_array[interval[0]] = max(end_position_array[interval[0]], interval[1])

        output = []
        tmp_interval = None
        for start, end in enumerate(end_position_array):
            if end is None:
                continue
            if tmp_interval is None:
                tmp_interval = [start, end]

            current_interval = [start, end]
            if max(tmp_interval[0], current_interval[0]) <= min(tmp_interval[1], current_interval[1]):
                tmp_interval[0] = min(tmp_interval[0], current_interval[0])
                tmp_interval[1] = max(tmp_interval[1], current_interval[1])
            else:
                output.append(tmp_interval)
                tmp_interval = current_interval

        if tmp_interval is not None:
            output.append(tmp_interval)

        return output
