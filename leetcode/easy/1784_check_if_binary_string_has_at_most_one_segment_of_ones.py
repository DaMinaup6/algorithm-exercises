# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def checkOnesSegment(self, s):
        got_one  = False
        got_zero = False
        
        for char in s:
            if char == '0':
                got_zero = True
            elif char == '1':
                if not got_one:
                    got_one = True
                elif got_one and got_zero:
                    return False

        return True
