// -----------------------------------------
// My Solution: Binary Search
//
// Time  complexity: O(k + log(n))
// Space Complexity: O(1)
// -----------------------------------------
// n := arr.size()
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int>::iterator right_iterator = lower_bound(arr.begin(), arr.end(), x);
        vector<int>::iterator left_iterator  = right_iterator - 1;
        while (right_iterator - left_iterator - 1 < k) {
            int right_num = (right_iterator < arr.end()) ? *right_iterator : MAX_NUM;
            int left_num = (left_iterator >= arr.begin()) ? *left_iterator : MAX_NUM;
            if (abs(left_num - x) <= abs(right_num - x))
                --left_iterator;
            else
                ++right_iterator;
        }

        return vector<int>(left_iterator + 1, right_iterator);
    }

private:
    static const int MAX_NUM = 1e9 + 7;
};

// -----------------------------------------
// Model Solution: Binary Search
//
// Time  complexity: O(k + log(n - k))
// Space Complexity: O(1)
// -----------------------------------------
// n := arr.size()
// Ref: https://leetcode.com/problems/find-k-closest-elements/solution/
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        // first element of output vector must exists in range [0...arr.size() - k]
        int left_cursor  = 0;
        int right_cursor = arr.size() - k;
        while (left_cursor < right_cursor) {
            int middle_cursor = (left_cursor + right_cursor) / 2;
            // only one of arr[middle_cursor] and arr[middle_cursor + k] could possibly be in a final answer
            // e.g. middle_cursor == 2 and k == 3, then arr[2] and arr[5] could not possibly both be in the answer
            if (x - arr[middle_cursor] > arr[middle_cursor + k] - x)
                left_cursor = middle_cursor + 1;
            else
                right_cursor = middle_cursor;
        }

        return vector<int>(arr.begin() + left_cursor, arr.begin() + left_cursor + k);
    }
};
