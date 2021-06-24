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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        int curr_position = 1;
        ListNode* reverse_prev_node = NULL;
        ListNode* curr_node = head;
        while (curr_position < left) {
            curr_position += 1;
            reverse_prev_node = curr_node;
            curr_node = curr_node->next;
        }

        ListNode* prev_node = NULL;
        while (curr_position <= right) {
            curr_position += 1;

            ListNode* next_node = curr_node->next;
            curr_node->next = prev_node;
            prev_node = curr_node;
            curr_node = next_node;
        }

        if (reverse_prev_node) {
            // e.g. 1->2->3->4->5, left == 2, right == 4
            //      => reverse_prev_node == 1
            //      after reverse 2->3->4 it becomes 4->3->2 and 1->2, we have prev_node == 4 and curr_node == 5
            //      now the next node of reverse_prev_node is still 2,
            //      so set 2->next == reverse_prev_node->next->next to be 5, which is curr_node
            //      and then update reverse_prev_node->next to be 4, which is prev_node
            reverse_prev_node->next->next = curr_node;
            reverse_prev_node->next = prev_node;
        } else {
            // e.g. 3->5->6, left == 1, right == 2
            //      in this case reverse_prev_node is NULL but the next node of head would be updated to NULL in
            //      while (curr_position <= right), so need to set head->next = curr_node
            head->next = curr_node;
        }
        return (left == 1 && right > left) ? prev_node : head;
    }
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := number of nodes of linked list
// Ref: https://leetcode.com/problems/reverse-linked-list-ii/discuss/1293063/C%2B%2B-Iterative-approach-%2B-explanation
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode *dummy_node = new ListNode(0);
        dummy_node->next = head;

        ListNode *prev_node = dummy_node, *curr_node;
        for (int position = 1; position < left; ++position) {
            prev_node = prev_node->next;
        }

        // e.g. 1 -> 2 -> 3 -> 4 -> 5
        //
        // At first iteration
        //   1 -> 2 -> 3 -> 4 -> 5
        //   ^    ^
        //   |    |
        // prev curr
        //      temp
        //
        // prev_node->next = curr_node->next;       => 1 -> 3
        // curr_node->next = curr_node->next->next; => 2 -> 4
        // prev_node->next->next = temp_node;       => 3 -> 2
        // => 1 -> 3 -> 2 -> 4 -> 5
        //
        // At secont iteration
        //   1 -> 3 -> 2 -> 4 -> 5
        //   ^    ^    ^
        //   |    |    |
        // prev temp curr
        //
        // prev_node->next = curr_node->next;       => 1 -> 4
        // curr_node->next = curr_node->next->next; => 2 -> 5
        // prev_node->next->next = temp_node;       => 4 -> 3
        // => 1 -> 4 -> 3 -> 2 -> 5
        curr_node = prev_node->next;
        for (int position = 1; position < right - left + 1; ++position) {
            ListNode *temp_node = prev_node->next;

            prev_node->next = curr_node->next;
            curr_node->next = curr_node->next->next;
            prev_node->next->next = temp_node;
        }
        return dummy_node->next;
    }
};
