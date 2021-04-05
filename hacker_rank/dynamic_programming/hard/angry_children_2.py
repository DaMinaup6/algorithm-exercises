# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n + k)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(packets)
# Ref: https://suzyz.github.io/2017/09/19/angry-children2/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryChildren function below.
def angryChildren(k, packets):
    packets.sort()

    prefix_sums = [packets[0]]
    for index in range(1, len(packets)):
        prefix_sums.append(packets[index] + prefix_sums[-1])

    curr_sum = 0
    # since packets sorted, so we can get unfairness sum in O(k) time
    # first k unfairness sum == sum_(i = 0)^(k - 1) i * p[i] - (k - 1 - i) * p[i]
    # where p := packets
    for index in range(k):
        curr_sum += index * packets[index] - (k - 1 - index) * packets[index]

    min_sum = curr_sum
    for index in range(1, len(packets) - k + 1):
        curr_sum = curr_sum + (k - 1) * (packets[index + k - 1] + packets[index - 1]) - 2 * (prefix_sums[index + k - 2] - prefix_sums[index - 1])
        min_sum  = min(min_sum, curr_sum)
    return min_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    packets = []

    for _ in range(n):
        packets_item = int(input())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()
