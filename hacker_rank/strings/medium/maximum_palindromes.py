# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(26 * (len(s) + q))
# Space Complexity: O(26 * len(s))
# -----------------------------------------
# Ref:
# a) https://www.hackerrank.com/challenges/maximum-palindromes/editorial
# b) https://www.hackerrank.com/challenges/maximum-palindromes/forum/comments/448266
# c) https://www.hackerrank.com/challenges/maximum-palindromes/forum/comments/629608

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def initialize(s):
    S, F, I = [[0] * 26 for _ in range(len(s) + 1)], [1] * len(s), [1] * len(s)
    for i, v in enumerate(s, 1):
        for j in range(26): # 2D array of character counts
            S[i][j] = S[i - 1][j] + (j == ord(v) - ord('a'))
    for i in range(1, len(s)):
        F[i] = F[i - 1] * i % MOD      # modular factorial
        I[i] = pow(F[i], MOD - 2, MOD) # modular inverse of factorial
    return (S, F, I)

#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r):
    c, s, d = 0, 0, 1
    for j in [S[r][i] - S[l - 1][i] for i in range(26)]:
        c += j % 2                  # count of center characters
        s += j // 2                 # count of side characters
        d *= I[j // 2]              # "denominators"
    return((c or 1) * F[s] * d % MOD)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    MOD = 26, 1000000007
    S, F, I = initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
