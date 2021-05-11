# -----------------------------------------
# My Solution: Greedy
#
# Time  Complexity: O(a + b + c)
# Space Complexity: O(a + b + c)
# -----------------------------------------
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        char_remains = [[a, 'a'], [b, 'b'], [c, 'c']]
        char_remains.sort(reverse=True)

        output_string = ""
        while char_remains[0][0] > 0:
            to_add_num_max = 2
            if len(output_string) > 0 and output_string[-1] == char_remains[0][1]:
                to_add_num_max = 1
            to_add_num = min(char_remains[0][0], to_add_num_max)

            output_string += char_remains[0][1] * to_add_num
            char_remains[0][0] -= to_add_num
            if char_remains[1][0] == 0:
                break
            else:
                output_string += char_remains[1][1]
                char_remains[1][0] -= 1

            char_remains.sort(reverse=True)

        return output_string
