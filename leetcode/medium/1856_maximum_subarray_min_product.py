# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(1)
# -----------------------------------------
# Note: This solution leads to TLE
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 1e9 + 7

        ans = 0
        for cursor in range(len(nums)):
            curr_num = nums[cursor]
            i = cursor - 1 if cursor - 1 >= 0 and nums[cursor - 1] >= curr_num else cursor
            j = cursor + 1 if cursor + 1 < len(nums) and nums[cursor + 1] >= curr_num else cursor
            while True:
                prev_i, prev_j = i, j
                if i >= 1 and nums[i - 1] >= curr_num:
                    i -= 1
                if j <= len(nums) - 2 and nums[j + 1] >= curr_num:
                    j += 1
                if i == prev_i and j == prev_j:
                    break    
            ans = max(ans, (curr_num * sum(nums[i:(j + 1)]) % MOD))

        return int(ans)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref:
# a) https://leetcode.com/problems/maximum-subarray-min-product/discuss/1198718/Python-Stack-keeps-index-of-element-less-than-numsi-O(N)
# b) https://leetcode.com/problems/maximum-subarray-min-product/discuss/1198896/O(n)-Monostack-with-picture
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        # e.g. nums == [3, 1, 5, 6, 4, 2] => l == [0, 0, 2, 3, 2, 2] and r == [0, 5, 3, 3, 4, 5]
        # for element 5 (index 2 in nums), l[2] == 2 and r[2] == 3 are the borders that element 5 is the min element in subarray nums[l[2]:(r[2] + 1)]
        l = [0] * n
        r = [0] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if len(stack) > 0:
                l[i] = stack[-1] + 1
            else:
                l[i] = 0
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if len(stack) > 0:
                r[i] = stack[-1] - 1
            else:
                r[i] = n - 1
            stack.append(i)

        max_product = 0
        for i in range(n):
            max_product = max(max_product, nums[i] * (pre_sum[r[i] + 1] - pre_sum[l[i]]))

        # don't use 1e9
        # Ref: https://stackoverflow.com/questions/67438654/is-x1e9-7-and-x109-7-different-in-python-if-yes-why
        return max_product % (10 ** 9 + 7)
