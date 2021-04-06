# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(1)
# -----------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    x.sort()
    
    transmitters = 0
    curr_range = []
    for index, house in enumerate(x):
        if len(curr_range) > 0:
            if curr_range[0] <= house <= curr_range[1]:
                continue
            else:
                curr_range = []

        if len(curr_range) == 0:
            transmitter_location = bisect.bisect_left(x, house + k)
            if transmitter_location < len(x) and x[transmitter_location] <= house + k:
                curr_range = [x[transmitter_location] - k, x[transmitter_location] + k]
            else:
                curr_range = [x[transmitter_location - 1] - k, x[transmitter_location - 1] + k]
            transmitters += 1

    return transmitters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
