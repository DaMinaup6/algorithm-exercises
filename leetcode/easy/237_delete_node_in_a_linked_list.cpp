/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(1)
// Space Complexity: O(1)
// -----------------------------------------
// Ref: https://leetcode.com/problems/delete-node-in-a-linked-list/discuss/65455/1-3-lines-C%2B%2BJavaPythonCCJavaScriptRuby
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode* next_node = node->next;
        // here `node` is a pointer
        // use an asterisk operator before `node` means to get the value stored in the memeory address held by pointer
        // so `*node = *next_node` means to replace the value stored in memeory address held by node
        // with value stored in memeory address held by next_node
        *node = *next_node;
        delete next_node;
    }
};
