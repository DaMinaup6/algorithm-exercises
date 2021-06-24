/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := number of nodes of linked list
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev_node = NULL;
        ListNode* curr_node = head;
        while (curr_node) {
            ListNode* next_node = curr_node->next;
            curr_node->next = prev_node;

            prev_node = curr_node;
            curr_node = next_node;
        }
        return prev_node;
    }
};
