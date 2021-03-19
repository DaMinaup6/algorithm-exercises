# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_range_dict = {}
        for index in range(len(S)):
            char = S[index]
            if char not in char_range_dict:
                char_range_dict[char] = [index, index]
            else:
                char_range_dict[char][1] = index

        ranges = list(char_range_dict.values())
        if len(ranges) == 1:
            return [len(S)]

        output = []
        cursor = 1
        curr_range = ranges[0]
        while cursor < len(ranges):
            if ranges[cursor][0] < curr_range[1]:
                curr_range[1] = max(curr_range[1], ranges[cursor][1])
            else:
                output.append(curr_range[1] - curr_range[0] + 1)
                curr_range = ranges[cursor]
            cursor += 1
        output.append(curr_range[1] - curr_range[0] + 1)

        return output

# -----------------------------------------
# Greedy
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_last_index_dict = {char: index for index, char in enumerate(S)}
        part_max_index = anchor = 0
        ans = []
        for index, char in enumerate(S):
            part_max_index = max(part_max_index, char_last_index_dict[char])
            if index == part_max_index:
                ans.append(index - anchor + 1)
                anchor = index + 1
            
        return ans
