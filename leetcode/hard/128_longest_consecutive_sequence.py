# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums):
        consecutive_dict = defaultdict(list) # { num: [start, end] }, which means from start to end is consecutive and num is in this range

        longest_consecutive = 0
        for num in nums:
            if num in consecutive_dict:
                continue
            # check if num - 1 or num + 1 already exists, if so then update the range
            min_num = consecutive_dict[num - 1][0] if num - 1 in consecutive_dict else num
            max_num = consecutive_dict[num + 1][1] if num + 1 in consecutive_dict else num
            # make sure the start number and end number holds the latest range
            # e.g. nums == [1, 3, 5, 2, 4, 0], when num == 4, consecutive_dict[1] still equals to [1, 3] if only do consecutive_dict[4] = [1, 5]
            #      so need to update consecutive_dict[1] and consecutive_dict[5] then we get the correct result if there exists 0 or 6 in nums
            consecutive_dict[num] = consecutive_dict[min_num] = consecutive_dict[max_num] = [min_num, max_num]
            longest_consecutive   = max(longest_consecutive, consecutive_dict[num][1] - consecutive_dict[num][0] + 1)

        return longest_consecutive

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)

        longest_consecutive = 0
        while len(nums_set) > 0:
            curr_num = nums_set.pop()
            prev_num = curr_num - 1
            while prev_num in nums_set:
                nums_set.remove(prev_num)
                prev_num -= 1
            next_num = curr_num + 1
            while next_num in nums_set:
                nums_set.remove(next_num)
                next_num += 1

            longest_consecutive = max(longest_consecutive, next_num - prev_num - 1)
        return longest_consecutive
