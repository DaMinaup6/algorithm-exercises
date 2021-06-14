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
// Time  Complexity: O(m + n)
// Space Complexity: O(1)
// -----------------------------------------
// m := number of nodes of l1, n := number of nodes of l2
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == NULL) return l2;
        if (l2 == NULL) return l1;

        // initialize new head of merged list
        ListNode* new_head;
        if (l1->val < l2->val) {
            new_head = l1;
            l1 = l1->next;
        } else {
            new_head = l2;
            l2 = l2->next;
        }

        // setup remaining nodes in while loop
        ListNode* curr_node = new_head;
        while (l1 != NULL || l2 != NULL) {
            if (l1 == NULL) {
                curr_node->next = l2;
                break;
            }
            if (l2 == NULL) {
                curr_node->next = l1;
                break;
            }

            if (l1->val < l2->val) {
                curr_node->next = l1;
                l1 = l1->next;
            } else {
                curr_node->next = l2;
                l2 = l2->next;
            }
            curr_node = curr_node->next;
        }

        return new_head;
    }
};
