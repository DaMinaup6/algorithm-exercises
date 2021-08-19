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
    int maxProduct(TreeNode* root) {
        calculate_root_sum(root);

        long max_product = 0;
        for (auto& it : root_sum) {
            if (it.first == root)
                continue;
            max_product = max(max_product, it.second * (root_sum[root] - it.second));
        }
        return max_product % MOD;
    }

private:
    static const int MOD = 1e9 + 7;
    unordered_map<TreeNode*, long> root_sum;

    long calculate_root_sum(TreeNode* root) {
        if (root == nullptr)
            return 0;
        if (root_sum[root] > 0)
            return root_sum[root];

        root_sum[root] = root->val + calculate_root_sum(root->left) + calculate_root_sum(root->right);
        return root_sum[root];
    }
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := number of nodes of tree
// Ref: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/discuss/1412813/C%2B%2BJavaPython-Post-Order-DFS-Clean-and-Concise

class Solution {
public:
    int maxProduct(TreeNode* root) {
        total_sum = calculate_root_sum_and_max_product(root);
        calculate_root_sum_and_max_product(root);
        return max_product % MOD;
    }

private:
    static const int MOD = 1e9 + 7;
    long total_sum;
    long max_product;

    long calculate_root_sum_and_max_product(TreeNode* root) {
        if (root == nullptr)
            return 0;

        long curr_sum = root->val + calculate_root_sum_and_max_product(root->left) + calculate_root_sum_and_max_product(root->right);
        max_product = max(max_product, curr_sum * (total_sum - curr_sum));
        return curr_sum;
    }
};
