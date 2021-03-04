# -----------------------------------------
# My Solution
# -----------------------------------------
class Solution:
    def jump(self, nums):
        # Strategy:
        #   * In each jump, find the landing point with farest position can reach among all possible landing points and jump to it
        #   * If farest position same for all possible landing points, choose the farest landing point
        jump_count = 0
        cursor = 0
        while cursor < len(nums) - 1:
            jump_max = nums[cursor]
            if cursor + jump_max >= len(nums) - 1:
                return jump_count + 1

            landing_infos = []
            for landing_index in range(cursor + 1, cursor + 1 + jump_max):
                landing_infos.append([landing_index + nums[landing_index], landing_index])
            next_index = sorted(landing_infos, key=lambda landing_info: (landing_info[0], landing_info[1]))[-1][1]

            cursor = next_index
            jump_count += 1

        return jump_count

processor = Solution()
print(f"processor.jump([2, 3, 1, 1, 4])                       == 2: {processor.jump([2, 3, 1, 1, 4]) == 2}")
print(f"processor.jump([2, 3, 0, 1, 4])                       == 2: {processor.jump([2, 3, 0, 1, 4]) == 2}")
print(f"processor.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 2: {processor.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 2}")
