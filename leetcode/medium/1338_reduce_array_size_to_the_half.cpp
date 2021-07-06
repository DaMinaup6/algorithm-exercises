// -----------------------------------------
// My Solution
//
// Time  Complexity: O(nlog(n))
// Space Complexity: O(n)
// -----------------------------------------
// n := arr.size()
class Solution {
public:
    int minSetSize(vector<int>& arr) {
        int arr_half_size = arr.size() / 2 + (arr.size() % 2);

        unordered_map<int, int> num_counter;
        for (int index = 0; index < arr.size(); ++index)
            ++num_counter[arr[index]];

        vector<int> num_counts;
        for (auto& key_value : num_counter)
            num_counts.push_back(key_value.second);
        sort(num_counts.begin(), num_counts.end());

        int removed_arr_size = 0;
        int min_set_size = 0;
        for (int index = num_counts.size() - 1; index >= 0; --index) {
            removed_arr_size += num_counts[index];
            ++min_set_size;
            if (removed_arr_size >= arr_half_size)
                break;
        }
        return min_set_size;
    }
};

// -----------------------------------------
// Model Solution: Bucket Sort
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := arr.size()
//
// Ref: https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Bucket-Sort-O(N)-Clean-and-Concise
class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int, int> cnt;
        for (int x : arr) ++cnt[x];

        vector<int> bucket(arr.size() + 1);
        int max_freq = 1;
        for (auto [_, freq] : cnt) {
            ++bucket[freq];
            max_freq = max(max_freq, freq);
        }

        int ans = 0, removed = 0, half = arr.size() / 2 + (arr.size() % 2), freq = max_freq;
        while (removed < half) {
            while (bucket[freq] == 0)
                --freq;
            --bucket[freq];

            removed += freq;
            ++ans;
        }
        return ans;
    }
};
