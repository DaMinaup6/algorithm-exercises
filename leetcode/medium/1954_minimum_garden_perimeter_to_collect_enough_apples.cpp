// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n^(1 / 3))
// Space Complexity: O(1)
// -----------------------------------------
// n := neededApples
class Solution {
public:
    long long minimumPerimeter(long long neededApples) {
        long long curr_apples = 12;
        long long one_side_apples = 5;
        long long curr_half_side_length = 1;
        while (curr_apples < neededApples) {
            /*
            each time we expand the square, the number of extra apples included == (current apples on one side + length of one side + apples on the expanded corner) * 4

            e.g. from square with side length 2 to square with side length 4

            (-1, +1) (+0, +1) (+1, +1)
            (-1, +0)          (+1, +0)
            (-1, -1) (+0, -1) (+1, -1)

            (-2, +2)   (-1, +2) (+0, +2) (+1, +2)   (+2, +2)
                     ↖︎              ↑             ↗
            (-2, +1)   (-1, +1) (+0, +1) (+1, +1)   (+2, +1)
            (-2, +0) ← (-1, +0)          (+1, +0) → (+2, +0)
            (-2, -1)   (-1, -1) (+0, -1) (+1, -1)   (+2, -1)
                     ↙              ↓             ↘
            (-2, -2)   (-1, -2) (+0, -2) (+1, -2)   (+2, -2)
            */
            curr_apples += (one_side_apples + (curr_half_side_length * 2 + 1) + (curr_half_side_length + 1) * 2) * 4;
            one_side_apples = one_side_apples + (curr_half_side_length * 2 + 1) + (curr_half_side_length + 1) * 4;
            curr_half_side_length += 1;
        }

        return curr_half_side_length * 8;
    }
};

// -----------------------------------------
// Model Solution: Cardano's formula
//
// Time  Complexity: O(1)
// Space Complexity: O(1)
// -----------------------------------------
// Ref: https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/discuss/1375396/O(1)-Cardano's-formula
class Solution {
public:
    long long minimumPerimeter(long long neededApples) {
        long long one_side_length = pow(neededApples * 2, 1.0 / 3);
        one_side_length += (one_side_length * (one_side_length + 1) * (one_side_length + 2) / 2) < neededApples;
        one_side_length += one_side_length % 2;

        return one_side_length * 4;
    }
};
