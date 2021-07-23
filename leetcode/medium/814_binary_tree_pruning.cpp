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
// Space Complexity: O(n)
// -----------------------------------------
// n := number of nodes of tree
class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        if (zero_tree(root))
            return NULL;

        root->left  = pruneTree(root->left);
        root->right = pruneTree(root->right);
        return root;
    }

private:
    unordered_map<TreeNode*, bool> root_zero_tree_map;

    bool zero_tree(TreeNode* root) {
        if (!root)
            return true;
        if (root_zero_tree_map.find(root) != root_zero_tree_map.end())
            return root_zero_tree_map[root];

        root_zero_tree_map[root] = root->val == 0 && zero_tree(root->left) && zero_tree(root->right);
        return root_zero_tree_map[root];
    }
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(h)
// -----------------------------------------
// h := height of the tree, n := number of nodes of tree
//
// Ref: https://leetcode.com/problems/binary-tree-pruning/discuss/1356558/C%2B%2BPython-DFS-Post-Order-Clean-and-Concise-O(N)
class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        if (root == nullptr)
            return nullptr;

        root->left  = pruneTree(root->left);
        root->right = pruneTree(root->right);
        if (root->val == 0 && root->left == nullptr && root->right == nullptr)
            return nullptr;
        return root;
    }
};
