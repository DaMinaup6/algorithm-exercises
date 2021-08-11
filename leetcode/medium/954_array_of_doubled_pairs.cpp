// -----------------------------------------
// My Solution
//
// Time  Complexity: O(nlog(n))
// Space Complexity: O(n)
// -----------------------------------------
// n := arr.size()
class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        if (arr.size() == 0)
            return true;

        sort(arr.begin(), arr.end());

        unordered_map<int, int> num_counter;
        for (auto num : arr)
            num_counter[num] += 1;

        size_t left_cursor  = 0;
        size_t right_cursor = arr.size() - 1;
        while (left_cursor < right_cursor) {
            int curr_num;
            if (abs(arr[left_cursor]) >= abs(arr[right_cursor])) {
                curr_num = arr[left_cursor];
                ++left_cursor;
            } else {
                curr_num = arr[right_cursor];
                --right_cursor;
            }

            if (num_counter[curr_num] == 0)
                continue;
            if (curr_num % 2 == 1 || curr_num % 2 == -1 || num_counter.find(curr_num / 2) == num_counter.end() || num_counter[curr_num / 2] == 0)
                return false;
            --num_counter[curr_num];
            --num_counter[curr_num / 2];
        }

        return true;
    }
};
