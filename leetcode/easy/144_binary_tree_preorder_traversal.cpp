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
// Model Solution: Morris Traversal
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := number of nodes of tree
// Ref: https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45466/C%2B%2B-Iterative-Recursive-and-Morris-Traversal
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> preorder_nodes;
        while (root) {
            if (root->left) {
                TreeNode* predecessor = root->left;
                while (predecessor->right && predecessor->right != root) {
                    predecessor = predecessor->right;
                }

                if (predecessor->right) {
                    predecessor->right = NULL;
                    root = root->right;
                } else {
                    predecessor->right = root;
                    preorder_nodes.push_back(root->val);
                    root = root->left;
                }
            } else {
                preorder_nodes.push_back(root->val);
                root = root->right;
            }
        }

        return preorder_nodes;
    }
};
