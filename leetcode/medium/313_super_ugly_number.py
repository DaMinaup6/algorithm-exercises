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

        # Strategy: use found ugly_numbers to generate next ugly number with primes
        #
        # take primes == [2, 3] as example
        # 1. starts with initialized ugly number ugly_numbers == [1]
        # 2. initialize prime_multiples with primes to record current prime multiples, i.e. [2, 3] -> [4, 3] -> [6, 3] -> ...
        # 3. initialize curr_ugly_num_idx with [0] * len(primes), this variable is used to record the ugly number to multiply for prime
        # 4. while len(ugly_numbers) < n
        #    a. add min(prime_multiples) to ugly_numbers. In this case, after first iteration, ugly_numbers == [1, 2]
        #    b. now prime_multiples == [2, 3] and 2 == ugly_numbers[-1], so we need to update 2, which is prime_multiples[0]
        #    c. the index of 2 in prime_multiples is 0, so add 1 to curr_ugly_num_idx[0] and curr_ugly_num_idx[0] == 1
        #    d. curr_ugly_num_idx[0] == 1 means that prime_multiples[0] needed to be updated to ugly_numbers[1] * primes[0], where 1 comes from curr_ugly_num_idx[0]
        #    e. so prime_multiples[0] == ugly_numbers[1] * primes[0] == 2 * 2 == 4
        #    f. similarly, in next iteration we will update curr_ugly_num_idx[1] to 1 and prime_multiples[1] will be updated to ugly_numbers[1] * primes[1] == 6
        curr_ugly_num_idx = [0] * len(primes)
        prime_multiples = primes[:]
        while len(ugly_numbers) < n:
            ugly_numbers.append(min(prime_multiples))
            for num_index, prime_multiple in enumerate(prime_multiples):
                # e.g. primes == [2, 3] and prime_multiples == [6, 6], curr_ugly_num_idx == [2, 1] and ugly_numbers == [1, 2, 3, 4, 6]
                #      update curr_ugly_num_idx to [3, 2] so prime_multiples would be updated to [8, 9]
                if prime_multiple == ugly_numbers[-1]:
                    curr_ugly_num_idx[num_index] += 1
                    prime_multiples[num_index] = primes[num_index] * ugly_numbers[curr_ugly_num_idx[num_index]]

        return ugly_numbers[-1]

# -----------------------------------------
# Enhanced Model Solution
#
# Time  Complexity: O((m + n)log(m))
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(primes)
# Note: Use heap to aviod calculate min in each iteration
# Ref:  https://ithelp.ithome.com.tw/articles/10232208
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_numbers = [1]

        # prime_infos[i] := (num, original_prime, ugly_num_index)
        prime_infos = []
        for index, prime in enumerate(primes):
            heapq.heappush(prime_infos, (prime, prime, 0))

        while len(ugly_numbers) < n:
            ugly_numbers.append(prime_infos[0][0])
            while prime_infos[0][0] == ugly_numbers[-1]:
                num, original_prime, ugly_num_index = heapq.heappop(prime_infos)
                ugly_num_index += 1
                num = original_prime * ugly_numbers[ugly_num_index]
                heapq.heappush(prime_infos, (num, original_prime, ugly_num_index))

        return ugly_numbers[-1]
