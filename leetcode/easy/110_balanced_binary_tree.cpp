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
// Time  Complexity: O(n^2)
// Space Complexity: O(n)
// -----------------------------------------
// n := number of nodes of tree
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (!root)
            return true;
        if (abs(tree_height(root->left) - tree_height(root->right)) > 1)
            return false;
        return isBalanced(root->left) && isBalanced(root->right);
    }

private:
    int tree_height(TreeNode* root) {
        if (!root)
            return 0;
        return 1 + max(tree_height(root->left), tree_height(root->right));
    }
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := number of nodes of tree
// Ref: https://leetcode.com/problems/balanced-binary-tree/discuss/35691/The-bottom-up-O(N)-solution-would-be-better
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return tree_height(root) != -1;
    }

private:
    int tree_height(TreeNode* root) {
        if (!root)
            return 0;

        int left_subtree_height = tree_height(root->left);
        if (left_subtree_height == -1)
            return -1;
        int right_subtree_height = tree_height(root->right);
        if (right_subtree_height == -1)
            return -1;
        if (abs(left_subtree_height - right_subtree_height) > 1)
            return -1;

        return 1 + max(left_subtree_height, right_subtree_height);
    }
};
