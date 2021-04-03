# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(n)
# -----------------------------------------
# m := max(len(bin(nums[i]))), n := len(nums)
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        nums_diff_count = collections.defaultdict(int)
        for num in nums:
            nums_diff_count[self.count_rev_diff(num)] += 1
        
        result = 0
        for rev_diff in nums_diff_count:
            result = (result + math.comb(nums_diff_count[rev_diff], 2)) % MOD
        return result
    
    def count_rev_diff(self, num):
        num_str = [char for char in str(num)]
        rev_num = 0
        for index in range(len(num_str) - 1, -1, -1):
            rev_num += int(num_str[index]) * 10 ** index
        return rev_num - num
