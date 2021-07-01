// -----------------------------------------
// My Solution: Dynamic Programming
//
// Time  complexity: O(2^n)
// Space Complexity: O(2^n)
// -----------------------------------------
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> curr_sequence = {0, 1};

        for (int layer = 1; layer < n; ++layer) {
            vector<int> next_sequence(1 << (layer + 1));
            for (int index = 0; index < curr_sequence.size(); ++index) {
                next_sequence[2 * index]     = curr_sequence[index] * 2 + (index % 2);
                next_sequence[2 * index + 1] = curr_sequence[index] * 2 + (1 - (index % 2));
            }
            curr_sequence = next_sequence;
        }
        return curr_sequence;
    }
};

// -----------------------------------------
// Model Solution
//
// Time  complexity: O(2^n)
// Space Complexity: O(2^n)
// -----------------------------------------
// Ref: https://leetcode.com/problems/gray-code/discuss/1308565/C%2B%2B-Simple-and-Short-Solution-O(n)-TC-O(1)-SC
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> gray_code_sequence(1 << n);

        // e.g. n == 2
        //
        // for layer == 0 => gray_code_sequence == [(000)_2, (001)_2]
        // for layer == 1 => gray_code_sequence == [(000)_2, (001)_2, (011)_2, (010)_2]
        //
        // we can see that from layer 0 to layer 1, we loop from back to head of sequence in layer 0, push (element | (1 << layer))
        // to new sequence then we get new sequence for next layer
        for (int layer = 0; layer < n; ++layer) {
            int sequence_size = 1 << layer;
            for (int index = sequence_size - 1; index >= 0; --index) {
                // assign element to index [sequence_size...(2 * sequence_size - 1)]
                gray_code_sequence[2 * sequence_size - index - 1] = gray_code_sequence[index] | (1 << layer);
            }
        }
        return gray_code_sequence;
    }
};
