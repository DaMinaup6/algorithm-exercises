# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def totalHammingDistance(self, nums):
        total_hamming_distance = 0

        digit_cursor = 1
        for i in range(32):
            digit_i_ones = 0
            # count how many num has 1 at digit i
            for num in nums:
                if num & digit_cursor > 0:
                    digit_i_ones += 1

            # digit_i_zeros * digit_i_ones == total_hamming_distance_at_i
            # e.g. nums == [001, 110, 010], for digit 1 the total hamming distance is == 1 * 2 == 2
            total_hamming_distance += (len(nums) - digit_i_ones) * digit_i_ones
            digit_cursor <<= 1

        return total_hamming_distance

processor = Solution()
print(f"processor.totalHammingDistance([2, 4, 13]): {processor.totalHammingDistance([2, 4, 13]) == 8}")
print(f"processor.totalHammingDistance([2, 4, 14]): {processor.totalHammingDistance([2, 4, 14]) == 6}")
print(f"processor.totalHammingDistance([2, 4, 15]): {processor.totalHammingDistance([2, 4, 15]) == 8}")
print(f"processor.totalHammingDistance([2, 5, 15]): {processor.totalHammingDistance([2, 5, 15]) == 8}")
