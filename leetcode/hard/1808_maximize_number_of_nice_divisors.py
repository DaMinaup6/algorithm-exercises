# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref:
# a) https://www.youtube.com/watch?v=xkqcceTrGJw
# b) https://math.stackexchange.com/a/1968962
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors <= 4:
            return primeFactors

        three_count = primeFactors // 3
        two_count = 0
        if primeFactors % 3 == 1:
            three_count -= 1
            two_count = 2
        elif primeFactors % 3 == 2:
            two_count = 1

        MOD = 1000000007
        if two_count > 0:
            return (pow(3, three_count, MOD) * pow(2, two_count, MOD)) % MOD
        return pow(3, three_count, MOD)
