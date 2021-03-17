# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
import math

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]

        output = [0, 1]
        power  = 1
        prev_start_index = 1
        curr_start_index = 2
        while curr_start_index <= num:
            middle_index = (curr_start_index * 3 - 1) // 2
            for index in range(curr_start_index, curr_start_index * 2):
                if index > num:
                    return output

                if index <= middle_index:
                    output.append(output[index - prev_start_index])
                else:
                    output.append(output[index - prev_start_index] + 1)

            power += 1
            prev_start_index = curr_start_index
            curr_start_index = int(math.pow(2, power))

        return output

# -----------------------------------------
# Simplified Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
import math

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]

        output = [0, 1]
        power  = 1
        curr_start_index = 2
        while curr_start_index <= num:
            for index in range(curr_start_index, curr_start_index * 2):
                if index > num:
                    return output
                output.append(output[index - curr_start_index] + 1)

            power += 1
            curr_start_index = int(math.pow(2, power))

        return output

'''Note: relationship between count of 1
 0     0 0 - initialized
 1     1 1 - initialized

============================

 2    10 1 - 0 count add 1
 3    11 2 - 1 count add 1

============================

 4   100 1 - 0 count add 1
 5   101 2 - 1 count add 1
 6   110 2 - 2 count add 1
 7   111 3 - 3 count add 1

============================

 8  1000 1 - 0 count add 1
 9  1001 2 - 1 count add 1
10  1010 2 - 2 count add 1
11  1011 3 - 3 count add 1
12  1100 2 - 4 count add 1
13  1101 3 - 5 count add 1
14  1110 3 - 6 count add 1
15  1111 4 - 7 count add 1
'''
