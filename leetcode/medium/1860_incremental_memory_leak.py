# -----------------------------------------
# My Solution
#
# Time  Complexity: O(math.sqrt(max(m, n)))
# Space Complexity: O(1)
# -----------------------------------------
# memory1 := m, memory2 := n
# Note: the reason why time complexity math.sqrt(max(m, n)) is because that for worst case we need to calculate which x satisfies 1 + 2 + ... + x >= max(m, n)
#       1 + 2 + ... + x == (x + 1) * x // 2 so we need to do math.sqrt(max(m, n)) times at most
#       but the actual time complexity would be faster since we use binary search here
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        memories = {1: memory1, 2: memory2}

        curr_second = 1
        while curr_second <= memories[1] or curr_second <= memories[2]:
            memory_diff  = abs(memories[1] - memories[2])
            larger_index = 1 if memories[1] >= memories[2] else 2

            if curr_second >= memory_diff:
                memories[larger_index] -= curr_second
                curr_second += 1
            else:
                # e.g. memory1 == 19, memory2 == 97
                # use binary search to find out that we allocate memories to memory stick 2 from 1st second to 13th second since (1 + 13) * 13 // 2 == 91
                # then after that we set memory2 to 6 and curr_second to 14
                left_pointer, right_pointer = curr_second, memories[larger_index]
                while left_pointer <= right_pointer:
                    middle_pointer = (left_pointer + right_pointer) // 2
                    middle_sum = (middle_pointer + curr_second) * (middle_pointer - curr_second + 1) // 2
                    if middle_sum > memory_diff:
                        right_pointer = middle_pointer - 1
                    else:
                        left_pointer = middle_pointer + 1
                memories[larger_index] -= (right_pointer + curr_second) * (right_pointer - curr_second + 1) // 2
                curr_second = right_pointer + 1

        return [curr_second, memories[1], memories[2]]

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------
# Ref:  https://leetcode.com/problems/incremental-memory-leak/discuss/1210210/Python-O(1)-Solution
# TODO: understand the logic
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        inverted = False
        if memory2 > memory1:
            memory2, memory1 = memory1, memory2
            inverted = True

        # Compute the number of steps in first stage - 1
        def solve_quadratic(i, x):
            return floor((-i + sqrt(i ** 2 + 4 * x)) / 2)
        i_start = solve_quadratic(1, 2 * (memory1 - memory2))

        # memory1 after the end of first stage is computed using the sum of arithmetic sequence
        memory1 -= i_start * (i_start + 1) // 2

        # Special case (if we end up with equal numbers after stage - 1 - undo inversion)
        if memory1 == memory2:
            inverted = False

        # Compute number of steps in stage - 2
        n_end = solve_quadratic((i_start + 1), memory2)

        # Compute sums of respective arithmetic sequences
        i_end_1 = i_start - 1 + 2 * n_end
        i_end_2 = i_start + 2 * n_end

        sum1 = n_end * (i_start + 1 + i_end_1) // 2
        sum2 = n_end * (i_start + 2 + i_end_2) // 2

        # Compute updated memories
        memory1 -= sum1
        memory2 -= sum2

        full_cnt = 2 * n_end + i_start

        if memory1 >= i_end_2 + 1: # If we can still make one removal from the first stick - perform it.
            memory1 -= i_end_2 + 1
            full_cnt += 1
        return [full_cnt + 1, memory2, memory1] if inverted else [full_cnt + 1, memory1, memory2]
