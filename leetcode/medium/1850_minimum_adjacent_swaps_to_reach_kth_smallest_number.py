# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^2 + kn)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(num)
# Ref: https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/discuss/1186823/Python-3-brute-force
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        origin_num_arr = [char for char in num]
        target_num_arr = origin_num_arr[:]
        for _ in range(k):
            self.next_permutation(target_num_arr)

        swap_count = 0
        for i in range(len(target_num_arr)):
            j = i
            while j < len(target_num_arr) and target_num_arr[i] != origin_num_arr[j]:
                j += 1
            swap_count += j - i

            origin_num_arr[i:(j + 1)] = [origin_num_arr[j]] + origin_num_arr[i:j]

        return swap_count

    def next_permutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        i += 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
