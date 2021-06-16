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
// Ref: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45550/C%2B%2B-Iterative-Recursive-and-Morris-Traversal
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> postorder_nodes;
        // get nodes in root - right - left order and revert nodes
        while (root) {
            if (root->right) {
                TreeNode* predecessor = root->right;
                while (predecessor->left && predecessor->left != root) {
                    predecessor = predecessor->left;
                }

                if (predecessor->left) {
                    predecessor->left = NULL;
                    root = root->left;
                } else {
                    predecessor->left = root;
                    postorder_nodes.push_back(root->val);
                    root = root->right;
                }
            } else {
                postorder_nodes.push_back(root->val);
                root = root->left;
            }
        }

        reverse(postorder_nodes.begin(), postorder_nodes.end());
        return postorder_nodes;
    }
};
