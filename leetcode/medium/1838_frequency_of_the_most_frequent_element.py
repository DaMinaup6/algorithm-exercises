# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # O(nlog(n))
        nums.sort()

        # O(n)
        left_pointer, right_pointer = len(nums) - 2, len(nums) - 1
        remaining_operations = k
        max_frequency = 1
        # find max_frequency of each element starts from rightmost element
        # e.g. k == 6, nums == [1, 2, 4, 6] => add 2 to third element and add 4 to second element we get [1, 6, 6, 6],
        # this gives us max_frequency == 3 and remaining_operations == 0
        #
        # now nums == [1, 6, 6, 6], for third element 4 we want as many elements as possible to equal 4. Since second element can be added to fourth element, which is 6,
        # so second element must be possible to equal to 4 (since 4 < 6), so at least we can have nums == [1, 4, 4, 6]
        # for this case, add (6 - 4) * (3 - 1) == 4 to remaining_operations since (3 - 1) elements changed from 6 to 4, where 3 == frequency of prev element
        # so now right_pointer == 2, left_pointer == 0 and remaining_operations == 4, which gives us nums == [4, 4, 4, 6], so max_frequency stays 3
        while left_pointer >= 0:
            # spend remaining_operations to move left_pointer
            while left_pointer >= 0 and remaining_operations >= nums[right_pointer] - nums[left_pointer]:
                remaining_operations -= nums[right_pointer] - nums[left_pointer]
                left_pointer -= 1

            curr_frequency = right_pointer - left_pointer
            max_frequency  = max(max_frequency, curr_frequency)
            # prepare for next element to count max frequency
            remaining_operations += (curr_frequency - 1) * (nums[right_pointer] - nums[right_pointer - 1])
            right_pointer -= 1
            left_pointer   = min(left_pointer, right_pointer - 1) # left_pointer won't move for cases like k == 2, nums == [3, 9, 6], so left_pointer should be at least right_pointer - 1

        return max_frequency
