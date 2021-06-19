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
// Model Solution: Reverse List + Two Pointers
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := number of nodes of linked list
// Ref: https://blog.csdn.net/coder_orz/article/details/51306985
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* slow_pointer = head;
        ListNode* fast_pointer = head;
        while (fast_pointer && fast_pointer->next) {
            slow_pointer = slow_pointer->next;
            fast_pointer = fast_pointer->next->next;
        }

        ListNode* reversed_head = reverse_linked_list(slow_pointer);
        while (reversed_head) {
            if (head->val != reversed_head->val)
                return false;
            head = head->next;
            reversed_head = reversed_head->next;
        }
        return true;
    }

    ListNode* reverse_linked_list(ListNode* head) {
        ListNode* prev_node = NULL;
        ListNode* curr_node = head;
        ListNode* next_node;
        while (curr_node) {
            next_node = curr_node->next;

            curr_node->next = prev_node;
            prev_node = curr_node;
            curr_node = next_node;
        }

        return prev_node;
    }
};
