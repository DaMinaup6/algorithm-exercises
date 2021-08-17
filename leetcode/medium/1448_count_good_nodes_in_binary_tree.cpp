/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := number of nodes in tree

class Solution {
public:
    int goodNodes(TreeNode* root) {
        count_good_nodes(root, INT_MIN);
        return good_nodes_count;
    }

private:
    int good_nodes_count = 0;

    void count_good_nodes(TreeNode* node, const int curr_max_val) {
        if (node == nullptr)
            return;

        if (node->val >= curr_max_val)
            ++good_nodes_count;

        const int next_max_val = max(curr_max_val, node->val);
        count_good_nodes(node->left,  next_max_val);
        count_good_nodes(node->right, next_max_val);
    }
};
