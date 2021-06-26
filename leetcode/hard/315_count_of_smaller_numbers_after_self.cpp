// -----------------------------------------
// My Solution: Bisect Insort
//
// Time  Complexity: O(n^2 + nlog(n))
// Space Complexity: O(n)
// -----------------------------------------
// n := nums.size()
// Note: This solution leads to TLE
#include <algorithm>

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> smaller_count(nums.size(), 0);
        vector<int> curr_nums = {nums.back()};

        for (int index = nums.size() - 2; index >= 0; --index) {
            int curr_num = nums[index];

            vector<int>::iterator insert_iterator = lower_bound(curr_nums.begin(), curr_nums.end(), curr_num);
            smaller_count[index] = insert_iterator - curr_nums.begin();
            curr_nums.insert(insert_iterator, curr_num);
        }
        return smaller_count;
    }
};

// -----------------------------------------
// Modle Solution: Binary Search Tree
//
// Time  Complexity: O(nlog(n)) ~ O(n^2)
// Space Complexity: O(n)
// -----------------------------------------
// n := nums.size()
// Ref:  https://www.youtube.com/watch?v=2SVLYsq5W8M
// Note: This solution leads to TLE
struct BSTNode {
    int val;
    int count;
    int left_count;
    BSTNode* left;
    BSTNode* right;

    BSTNode(int val): val(val), count(1), left_count(0), left(nullptr), right(nullptr) {}
    ~BSTNode() {
        delete left;
        delete right;
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        unique_ptr<BSTNode> bst_root_unique_ptr(new BSTNode(nums.back()));

        vector<int> smaller_on_right_count = {0};
        for (int index = nums.size() - 2; index >= 0; --index) {
            smaller_on_right_count.push_back(insert_node(bst_root_unique_ptr.get(), nums[index]));
        }
        reverse(smaller_on_right_count.begin(), smaller_on_right_count.end());

        return smaller_on_right_count;
    }

private:
    // return the number of elements smaller than insert_val under root
    int insert_node(BSTNode* root_ptr, int insert_val) {
        if (root_ptr->val == insert_val) {
            ++root_ptr->count;
            return root_ptr->left_count;
        } else if (insert_val < root_ptr->val) {
            ++root_ptr->left_count;

            if (root_ptr->left == nullptr) {
                root_ptr->left = new BSTNode(insert_val);
                // clearly there is no elements with value smaller than insert_val for this case so return 0
                return 0;
            }
            return insert_node(root_ptr->left, insert_val);
        } else {
            int smaller_nodes_count = root_ptr->count + root_ptr->left_count;
            if (root_ptr->right == nullptr) {
                root_ptr->right = new BSTNode(insert_val);
                return smaller_nodes_count;
            }
            return smaller_nodes_count + insert_node(root_ptr->right, insert_val);
        }
    }
};

// -----------------------------------------
// Modle Solution: Binary Indexed Tree
//
// Time  Complexity: O(nlog(n))
// Space Complexity: O(n)
// -----------------------------------------
// n := nums.size()
// Ref: https://www.youtube.com/watch?v=2SVLYsq5W8M
#include <set>

class BinaryIndexedTree {
public:
    BinaryIndexedTree(int tree_size): binary_indexed_tree(tree_size, 0) {}

    void update(int index, int delta) {
        // Note: here we use binary_indexed_tree.size() so operator is <
        //       The reason we use <= in problem 307 is because index compared with nums.size() there,
        //       where nums.size() + 1 == binary_indexed_tree.size() in problem 307
        while (index < binary_indexed_tree.size()) {
            binary_indexed_tree[index] += delta;
            index += low_bit(index);
        }
    }

    int range_sum(int index) {
        int range_sum = 0;

        while (index > 0) {
            range_sum += binary_indexed_tree[index];
            index -= low_bit(index);
        }
        return range_sum;
    }

private:
    vector<int> binary_indexed_tree;

    static inline int low_bit(int num) {
        return num & (-num);
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        sorted_nums_set = set<int>(nums.begin(), nums.end());
        int curr_rank = 1;
        for (const int num : sorted_nums_set) {
            num_ranks[num] = curr_rank;
            ++curr_rank;
        }
        BinaryIndexedTree binary_indexed_tree(num_ranks.size() + 1);

        // e.g. nums == [5, 2, 6, 1] => num_ranks == { 1: 1, 2: 2, 5: 3, 6: 4 }
        //      for 1, there is no element on its right                         -> get 0, update tree by adding one rank 1 element
        //      for 6, we have one rank 1 element stored in binary indexed tree -> get 1, update tree by adding one rank 4 element
        //      for 2, we have one rank 1 element stored in binary indexed tree -> get 1, update tree by adding one rank 2 element
        //      for 5, we have one rank 1 element and one rank 2 element        -> get 2, update tree by adding one rank 3 element
        vector<int> smaller_on_right_count;
        for (int index = nums.size() - 1; index >= 0; --index) {
            int num_rank = num_ranks[nums[index]];
            int smaller_count = binary_indexed_tree.range_sum(num_rank - 1);

            smaller_on_right_count.push_back(smaller_count);
            binary_indexed_tree.update(num_rank, 1);
        }

        reverse(smaller_on_right_count.begin(), smaller_on_right_count.end());
        return smaller_on_right_count;
    }

private:
    set<int> sorted_nums_set;
    unordered_map<int, int> num_ranks;
};
