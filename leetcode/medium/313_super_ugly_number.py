# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(primes)
# Ref: https://ithelp.ithome.com.tw/articles/10232208
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_numbers = [1]

        curr_ugly_num_idx = [0] * len(primes)
        prime_multiples = primes.copy()
        while len(ugly_numbers) < n:
            ugly_numbers.append(min(prime_multiples))
            for num_index, prime_multiple in enumerate(prime_multiples):
                # e.g. primes == [2, 3] and prime_multiples == [6, 6], curr_ugly_num_idx == [2, 1] and ugly_numbers == [1, 2, 3, 4, 6]
                #      update curr_ugly_num_idx to [3, 2] so prime_multiples would be updated to [8, 9]
                if prime_multiple == ugly_numbers[-1]:
                    curr_ugly_num_idx[num_index] += 1
                    prime_multiples[num_index] = primes[num_index] * ugly_numbers[curr_ugly_num_idx[num_index]]

        return ugly_numbers[-1]
