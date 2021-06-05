# -----------------------------------------
# My Solution: Dynamic Programming + Binary Search
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
import bisect

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        self.arr = arr
        # dp[i] := [can reach end or not by applying odd jump first fron index i, can reach end or not by applying even jump first fron index i]
        dp = [[False, False] for _ in range(len(arr))]
        dp[-1] = [True, True]

        checked_nums = sorted([(arr[-1], len(arr) - 1)]) # sorted array with element (num, num index in arr)
        good_indices = 1
        for index in range(len(arr) - 2, -1, -1):
            # find next odd jump position, if we can reach end by applying even jump first at that position then record dp[index][0] as True
            next_jump_index = self.find_next_odd_jump_index(index, checked_nums)
            if next_jump_index >= 0 and dp[next_jump_index][1]:
                dp[index][0] = True
                good_indices += 1
            # find next even jump position, if we can reach end by applying odd jump first at that position then record dp[index][1] as True
            next_jump_index = self.find_next_even_jump_index(index, checked_nums)
            if next_jump_index >= 0 and dp[next_jump_index][0]:
                dp[index][1] = True
            # add current num to checked_nums for remaining numbers
            bisect.insort(checked_nums, (arr[index], index))

        return good_indices

    def find_next_odd_jump_index(self, start_index, checked_nums):
        curr_num = self.arr[start_index]
        checked_nums_index = bisect.bisect_left(checked_nums, (curr_num, start_index))
        if checked_nums_index < len(checked_nums):
            return checked_nums[checked_nums_index][1]
        return -1

    def find_next_even_jump_index(self, start_index, checked_nums):
        curr_num = self.arr[start_index]
        checked_nums_index = bisect.bisect_left(checked_nums, (curr_num, start_index))
        if checked_nums_index == len(checked_nums):
            checked_nums_index -= 1
        if checked_nums[checked_nums_index][0] > curr_num:
            checked_nums_index -= 1
            if checked_nums_index < 0:
                return -1
        # need choose the smallest index
        # e.g. arr == [3, 1, 1, 4] and start_index == 0 and now we have checked_nums == [(1, 1), (1, 2), (4, 3)]
        #      after apply bisect_left, we get checked_nums_index == 2
        #      since we are applying even jump now, so we need to find element <= 3
        #      so we minus checked_nums_index by 1, we find element 1 which is less than or equal to 3
        #      but there are multiple indexes for this element, so apply bisect_left again to find element 1 with smallest index
        next_num = checked_nums[checked_nums_index][0]
        checked_nums_index = bisect.bisect_left(checked_nums, (next_num, start_index))
        if checked_nums_index >= 0:
            return checked_nums[checked_nums_index][1]
        return -1

# -----------------------------------------
# Model Solution: Dynamic Programming + Stack
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC%2B%2BPython-DP-using-Map-or-Stack
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        sorted_arr = sorted([(num, index) for index, num in enumerate(arr)])

        # e.g. arr == [10, 13, 12, 14, 15], next_higher would be [2, 3, 3, 4, -1]
        next_higher = [-1] * len(arr)
        stack = []
        for num, index in sorted((num, index) for index, num in enumerate(arr)):
            while len(stack) > 0 and stack[-1] < index:
                next_higher[stack.pop()] = index
            stack.append(index)

        # e.g. arr == [10, 13, 12, 14, 15], next_higher would be [-1, 2, -1, -1, -1]
        next_lower = [-1] * len(arr)
        stack = []
        # cannot do sorted_arr[::-1] here, since we need something like [(4, 2), (1, 0), (1, 1)]
        # if we do sorted_arr[::-1] then we get [(4, 2), (1, 1), (1, 0)]
        for num, index in sorted((-num, index) for index, num in enumerate(arr)):
            while len(stack) > 0 and stack[-1] < index:
                next_lower[stack.pop()] = index
            stack.append(index)

        # dp[i] := [can reach end or not by applying odd jump first fron index i, can reach end or not by applying even jump first fron index i]
        dp = [[False, False] for _ in range(len(arr))]
        dp[-1] = [True, True]

        good_indices = 1
        for index in range(len(arr) - 2, -1, -1):
            next_odd_jump_index = next_higher[index]
            if next_odd_jump_index != -1 and dp[next_odd_jump_index][1]:
                dp[index][0] = True
                good_indices += 1

            next_even_jump_index = next_lower[index]
            if next_even_jump_index != -1 and dp[next_even_jump_index][0]:
                dp[index][1] = True

        return good_indices
