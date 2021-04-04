# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nd)
# Space Complexity: O(k)
# -----------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

def median_of(nums):
    if len(nums) % 2 == 0:
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
    else:
        return nums[len(nums) // 2]

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    curr_nums = sorted(expenditure[:d])
    curr_median = median_of(curr_nums)

    notifications = 0
    for index in range(d, len(expenditure)):
        if expenditure[index] >= 2 * curr_median:
            notifications += 1
        if index < len(expenditure) - 1:
            curr_nums.pop(bisect.bisect_left(curr_nums, expenditure[index - d]))
            bisect.insort(curr_nums, expenditure[index])
            curr_median = median_of(curr_nums)

    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
