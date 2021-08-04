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
// Space Complexity: O(h)
// -----------------------------------------
// n := number of nodes in tree, h := maximum height of tree
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        if (!root)
            return {};

        target_sum = targetSum;
        vector<int> curr_path = {root->val};
        generate_paths(root, root->val, curr_path);
        return all_paths;
    }

private:
    vector<vector<int>> all_paths;
    int target_sum;

    void generate_paths(TreeNode* node, int curr_sum, vector<int>& curr_path) {
        if (!node->left && !node->right) {
            if (curr_sum == target_sum)
                all_paths.push_back(curr_path);
            return;
        }

        if (node->left) {
            curr_path.push_back(node->left->val);
            generate_paths(node->left, curr_sum + node->left->val, curr_path);
            curr_path.pop_back();
        }

        if (node->right) {
            curr_path.push_back(node->right->val);
            generate_paths(node->right, curr_sum + node->right->val, curr_path);
            curr_path.pop_back();
        }
    }
};
