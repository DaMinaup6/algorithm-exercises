# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        tmp_arr_size = 0
        last_max = -1
        curr_max = -1
        chunks = 0
        for index in range(len(arr)):
            if arr[index] > curr_max:
                curr_max = arr[index]
            tmp_arr_size += 1
            if tmp_arr_size == curr_max - last_max:
                tmp_arr_size = 0
                last_max = curr_max
                curr_max += 1
                chunks += 1
        return chunks

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = curr_max = 0
        for index, num in enumerate(arr):
            curr_max = max(curr_max, num)
            if curr_max == index:
                chunks += 1
        return chunks
