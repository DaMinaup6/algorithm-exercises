// -----------------------------------------
// Model Solution: Sieve of Eratosthenes
//
// Time  Complexity: O(n * log(log(n)))
// Space Complexity: O(n)
// -----------------------------------------
// Ref:
// a) https://leetcode.com/problems/count-primes/solution/
// b) https://leetcode.com/problems/count-primes/discuss/57601/Short-C%2B%2B-Sieve-of-Eratosthenes-solution
// c) https://leetcode.com/problems/count-primes/discuss/473021/Time-Complexity-O(log(log(n))-Explained
// d) https://www.youtube.com/watch?v=I6HrVRGGYNI
class Solution {
public:
    int countPrimes(int n) {
        if (n <= 1)
            return 0;

        vector<bool> num_is_prime(n, true);
        int primes_count = 0;

        num_is_prime[0] = num_is_prime[1] = false;
        for (int num = 2; num < n; ++num) {
            if (num_is_prime[num]) {
                for (int composite_num = 2 * num; composite_num < n; composite_num += num) {
                    num_is_prime[composite_num] = false;
                }
                primes_count += 1;
            }
        }
        return primes_count;
    }
};
