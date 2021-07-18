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
// n := number of nodes in the list
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *new_head = NULL, *curr_group_tail = NULL, *next_group_head = head;
        while (true) {
            vector<ListNode*> reverse_result = reverse_list(next_group_head, k);
            // for first group reverse
            if (!new_head)
                new_head = reverse_result[0];
            if (curr_group_tail)
                curr_group_tail->next = reverse_result[0];

            curr_group_tail = next_group_head;
            next_group_head = reverse_result[1];
            if (!next_group_size_valid(next_group_head, k)) {
                curr_group_tail->next = next_group_head;
                break;
            }
        }
        return new_head;
    }

private:
    // do nothing if remain group size smaller than k
    bool next_group_size_valid(ListNode* head, int group_size) {
        ListNode* curr_node = head;
        int curr_group_size = 0;
        while (curr_node && curr_group_size < group_size) {
            curr_node = curr_node->next;
            ++curr_group_size;
        }
        return curr_group_size == group_size;
    }

    vector<ListNode*> reverse_list(ListNode* head, int group_size) {
        ListNode* prev_node = NULL;
        ListNode* curr_node = head;
        ListNode* next_node;
        int curr_group_size = 0;
        while (curr_node && curr_group_size < group_size) {
            next_node = curr_node->next;
            curr_node->next = prev_node;

            prev_node = curr_node;
            curr_node = next_node;
            ++curr_group_size;
        }
        return {prev_node, next_node};
    }
};
