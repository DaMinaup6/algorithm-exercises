/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */

// -----------------------------------------
// Model Solution
//
// Space Complexity: O(t)
// -----------------------------------------
// t := total of nodes after inserting all `key` string
//
// Ref: https://leetcode.com/problems/beautiful-array/discuss/186679/Odd-%2B-Even-Pattern-O(N)
struct TrieNode {
    TrieNode* children[26] = {};
    int sum = 0; // Store the sum of all strings go through this node.
};

class MapSum {
public:
    unordered_map<string, int> key_val_map;
    TrieNode trie_root;
    MapSum() {}

    // Time Complexity: O(k)
    // k := key.size()
    void insert(string key, int val) {
        int diff = val - key_val_map[key];

        TrieNode* curr_node = &trie_root;
        for (char letter: key) {
            letter -= 'a';
            if (curr_node->children[letter] == nullptr)
                curr_node->children[letter] = new TrieNode();
            curr_node = curr_node->children[letter];
            curr_node->sum += diff;
        }
        key_val_map[key] = val;
    }

    // Time Complexity: O(k)
    // k := prefix.size()
    int sum(string prefix) {
        TrieNode* curr_node = &trie_root;
        for (char letter: prefix) {
            letter -= 'a';
            if (curr_node->children[letter] == nullptr)
                return 0;
            curr_node = curr_node->children[letter];
        }
        return curr_node->sum;
    }
};
