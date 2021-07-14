// -----------------------------------------
// My Solution
//
// Time  Complexity: O(nlog(n))
// Space Complexity: O(n)
// -----------------------------------------
// n := str.size()
class Solution {
public:
    string customSortString(string order, string str) {
        for (char& letter: order)
            add_letter_order(letter);

        vector<int> str_orders;
        for (char& letter: str) {
            if (letter_order_map.find(letter) == letter_order_map.end())
                add_letter_order(letter);
            str_orders.push_back(letter_order_map[letter]);
        }

        sort(str_orders.begin(), str_orders.end());

        string sorted_str;
        for (int& order: str_orders)
            sorted_str.push_back(order_letter_map[order]);
        return sorted_str;
    }

private:
    unordered_map<char, int> letter_order_map;
    unordered_map<int, char> order_letter_map;

    void add_letter_order(char& letter) {
        int curr_order = letter_order_map.size();
        letter_order_map[letter] = curr_order;
        order_letter_map[curr_order] = letter;
    }
};

// -----------------------------------------
// Model Solution: Counting Sort
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := str.size()
//
// Ref:  https://leetcode.com/problems/custom-sort-string/discuss/1336524/C%2B%2BPython-Counting-Sort-Clean-and-Concise-O(N)
class Solution {
public:
    string customSortString(string order, string str) {
        int letter_counter[26] = {};
        for (char& letter: str)
            ++letter_counter[letter - 'a'];

        string sorted_str;
        // add characters with order defined to sorted_str
        for (char& letter: order) {
            while (letter_counter[letter - 'a'] > 0) {
                sorted_str.push_back(letter);
                --letter_counter[letter - 'a'];
            }
        }
        // add characters with order undefined to sorted_str
        for (char letter = 'a'; letter <= 'z'; ++letter) {
            while (letter_counter[letter - 'a'] > 0) {
                sorted_str.push_back(letter);
                --letter_counter[letter - 'a'];
            }
        }

        return sorted_str;
    }
};
