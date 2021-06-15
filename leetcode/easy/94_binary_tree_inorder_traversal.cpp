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
// Model Solution: Recursion
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := number of nodes of tree
// Ref: https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31231/C%2B%2B-Iterative-Recursive-and-Morris
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inorder_nodes;
        inorder_add_nodes(root, inorder_nodes);
        return inorder_nodes;
    }

private:
    void inorder_add_nodes(TreeNode* root, vector<int>& nodes) {
        if (root == NULL)
            return;

        inorder_add_nodes(root->left, nodes);
        nodes.push_back(root->val);
        inorder_add_nodes(root->right, nodes);
    }
};

// -----------------------------------------
// Model Solution: Morris Traversal
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := number of nodes of tree
// Ref:
// a) https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31231/C%2B%2B-Iterative-Recursive-and-Morris
// b) https://www.youtube.com/watch?v=wGXB9OWhPTg
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inorder_nodes;
        while (root) {
            if (root->left) {
                TreeNode* predecessor = root->left;
                while (predecessor->right && predecessor->right != root) {
                    predecessor = predecessor->right;
                }

                if (predecessor->right) {
                    predecessor->right = NULL;
                    inorder_nodes.push_back(root->val);
                    // root here is the rightmost child of the left sub-tree, its right child was set
                    // to original root previously so `root = root->right;` means go back to original root
                    root = root->right;
                } else {
                    // create temporary link to go back to root after loop through left sub-tree
                    predecessor->right = root;
                    root = root->left;
                }
            } else {
                inorder_nodes.push_back(root->val);
                root = root->right;
            }
        }

        return inorder_nodes;
    }
};
