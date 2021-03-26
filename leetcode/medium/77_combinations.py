# -----------------------------------------
# My Solution
#
# Time  Complexity: O(math.comb(n, k))
# Space Complexity: O(math.comb(n, k))
# -----------------------------------------
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def generate_combination(start_num, combination):
            if len(combination) == k:
                combinations.append(combination)
                return
            for num in range(start_num + 1, n + 1):
                generate_combination(num, combination + [num])
        
        generate_combination(0, [])
        return combinations

# -----------------------------------------
# Backtracking
#
# Time  Complexity: O(math.comb(n, k))
# Space Complexity: O(math.comb(n, k))
# -----------------------------------------
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def generate_combination(combination, curr_size, start_num):
            if curr_size == k:
                combinations.append(combination.copy())
                return
            for num in range(start_num, n + 1):
                combination[curr_size] = num
                curr_size += 1
                generate_combination(combination, curr_size, num + 1)
                curr_size -= 1
        
        generate_combination([0] * k, 0, 1)
        return combinations
