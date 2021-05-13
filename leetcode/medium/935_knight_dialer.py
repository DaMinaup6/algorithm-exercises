# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        curr_num_next_numbers_dict = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        curr_path_count_arr = [1] * 10
        for _ in range(n - 1):
            next_path_count_arr = [0] * 10
            for num in range(10):
                for next_number in curr_num_next_numbers_dict[num]:
                    next_path_count_arr[next_number] = (next_path_count_arr[next_number] + curr_path_count_arr[num]) % MOD
            curr_path_count_arr = next_path_count_arr
        return sum(curr_path_count_arr) % MOD

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/knight-dialer/discuss/189252/O(logN)
import numpy as np

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        MOD = 10 ** 9 + 7
        matrix = np.matrix([
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        ])

        res, n = 1, n - 1
        while n > 0:
            if n % 2 == 1:
                res = (res * matrix) % MOD
            matrix = (matrix * matrix) % MOD
            n //= 2
        return int(np.sum(res)) % MOD
