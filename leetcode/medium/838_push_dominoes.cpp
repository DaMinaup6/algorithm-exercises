// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := dominoes.size()
class Solution {
public:
    string pushDominoes(string dominoes) {
        int max_force = dominoes.size();

        vector<int> positive_net_forces(dominoes.size());
        for (int index = 0; index < dominoes.size(); ++index) {
            if (dominoes[index] == 'R')
                positive_net_forces[index] = max_force;
            else if (dominoes[index] != 'L' && index > 0 && positive_net_forces[index - 1] > 0)
                positive_net_forces[index] = positive_net_forces[index - 1] - 1;
        }

        vector<int> negative_net_forces(dominoes.size());
        for (int index = dominoes.size() - 1; index >= 0; --index) {
            if (dominoes[index] == 'L')
                negative_net_forces[index] = -max_force;
            else if (dominoes[index] != 'R' && index < dominoes.size() - 1 && negative_net_forces[index + 1] < 0)
                negative_net_forces[index] = negative_net_forces[index + 1] + 1;
        }

        string final_state_string(dominoes.size(), '.');
        for (int index = 0; index < dominoes.size(); ++index) {
            int net_force = positive_net_forces[index] + negative_net_forces[index];
            if (net_force != 0)
                final_state_string[index] = net_force > 0 ? 'R' : 'L';
        }
        return final_state_string;
    }
};

// -----------------------------------------
// Model Solution: Two Pointers
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := dominoes.size()
//
// Ref: https://leetcode.com/problems/push-dominoes/discuss/132332/JavaC%2B%2BPython-Two-Pointers
class Solution {
public:
    string pushDominoes(string dominoes) {
        dominoes = 'L' + dominoes + 'R';

        string final_state;
        for (int i = 0, j = 1; j < dominoes.length(); ++j) {
            if (dominoes[j] == '.')
                continue;

            int distance = j - i - 1;
            if (i > 0)
                final_state += dominoes[i];
            if (dominoes[i] == dominoes[j])
                final_state += string(distance, dominoes[i]);
            else if (dominoes[i] == 'L' && dominoes[j] == 'R')
                final_state += string(distance, '.');
            else
                final_state += string(distance / 2, 'R') + string(distance % 2, '.') + string(distance / 2, 'L');

            i = j;
        }
        return final_state;
    }
};
