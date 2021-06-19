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
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n^2)
// -----------------------------------------
// n := number of nodes of tree
// Ref: https://leetcode.com/problems/binary-tree-paths/discuss/1251332/C%2B%2B%3A-Recursive-solution
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        if (root == nullptr)
            return {};

        add_path(root, "");
        return paths;
    }

private:
    vector<string> paths;

    void add_path(TreeNode* curr_node, string curr_path) {
        if (curr_node == nullptr)
            return;

        if (curr_node->left == nullptr && curr_node->right == nullptr) {
            curr_path += to_string(curr_node->val);
            paths.push_back(curr_path);
        } else {
            curr_path += to_string(curr_node->val) + "->";
            add_path(curr_node->left,  curr_path);
            add_path(curr_node->right, curr_path);
        }
    }
};
