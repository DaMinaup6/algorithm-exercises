# -----------------------------------------
# Model Solution: Binary indexes Tree
#
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=WbafSgetDDk
class NumArray:

    # -----> Time Complexity: O(n)
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.binary_indexed_tree = [0] * (len(nums) + 1)
        for index in range(len(nums)):
            self.update_tree_val(index, nums[index])

    # -----> Time Complexity: O(1)
    def lowest_bit(self, num):
        return num & (-num)

    # -----> Time Complexity: O(log(n))
    def update_tree_val(self, index: int, diff: int) -> None:
        index += 1
        while index <= len(self.nums):
            self.binary_indexed_tree[index] += diff
            index += self.lowest_bit(index)

    # -----> Time Complexity: O(log(n))
    def get_sum(self, index: int) -> int:
        range_sum = 0

        index += 1
        while index > 0:
            range_sum += self.binary_indexed_tree[index]
            index -= self.lowest_bit(index)
        return range_sum

    # -----> Time Complexity: O(log(n))
    def update(self, index: int, val: int) -> None:
        self.update_tree_val(index, val - self.nums[index])
        self.nums[index] = val

    # -----> Time Complexity: O(log(n))
    def sumRange(self, left: int, right: int) -> int:
        return self.get_sum(right) - self.get_sum(left - 1)
