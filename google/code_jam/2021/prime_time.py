# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n * 2^n)
# Space Complexity: O(n)
# -----------------------------------------
# n := number of primes
# NOTE: this passes only test set 1
from functools import reduce
from itertools import combinations

def max_sum(cards_num):
    total_num = sum(num for _, num in cards_num.items())
    total_sum = sum(prime * num for prime, num in cards_num.items())
    all_prime = sum([[prime] * num for prime, num in cards_num.items()], [])
    max_score = 0
    for prime_num in range(1, total_num + 1):
        for combination in combinations(all_prime, prime_num):
            combination_sum  = sum(combination)
            combination_prod = reduce(lambda a, b: a * b, combination)
            if total_sum - combination_sum == combination_prod:
                max_score = max(max_score, total_sum - combination_sum)

    return max_score

t = int(input())
for case_index in range(1, t + 1):
    m = int(input())
    cards_num = {}
    for _ in range(m):
        p, n = [int(char) for char in input().split(' ')]
        cards_num[p] = n

    print("Case #{}: {}".format(case_index, max_sum(cards_num)))

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(PRODUCT_GROUP_SUM_MAX * (TOTAL_PRIMES + MAX_PRIME_NUM))
# Space Complexity: O(TOTAL_PRIMES)
# -----------------------------------------
from collections import defaultdict

PRIME_MAX = 499
TOTAL_PRIMES = 95
MAX_PRIME_NUM = 60 # p_i <= 499, sum(n_i) <= 10 ** 15, 2 ** 60 > 499 * 10 ** 15 => at most 60 primes in second group
PRODUCT_GROUP_SUM_MAX = 5000 # the upper bound would be MAX_PRIME_NUM * PRIME_MAX, but it cannot be that high so choose a relative small number

def max_sum(cards_num):
    total_sum = sum(prime * num for prime, num in cards_num.items())
    for second_group_sum in range(2, PRODUCT_GROUP_SUM_MAX + 1):
        first_group_sum = total_sum - second_group_sum
        total_prime_factor_num = 0
        divided_sum = 0
        for prime in cards_num:
            if first_group_sum <= 1 or divided_sum >= second_group_sum or total_prime_factor_num >= MAX_PRIME_NUM:
                break
            prime_power = 0
            while first_group_sum % prime == 0:
                first_group_sum //= prime
                prime_power += 1
                if prime_power >= cards_num[prime]:
                    break
            total_prime_factor_num += prime_power
            divided_sum += prime * prime_power
            if prime_power < cards_num[prime] and first_group_sum % prime == 0:
                break
        if first_group_sum == 1 and divided_sum == second_group_sum:
            return total_sum - second_group_sum
    return 0

t = int(input())
for case_index in range(1, t + 1):
    m = int(input())
    cards_num = {}
    for _ in range(m):
        p, n = [int(char) for char in input().split(' ')]
        cards_num[p] = n

    print("Case #{}: {}".format(case_index, max_sum(cards_num)))
