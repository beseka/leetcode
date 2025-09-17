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
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        // Create a dummy node to simplify edge cases
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;

        // Traverse the list and swap pairs
        while (head && head->next) {
            // Nodes to be swapped
            ListNode* first = head;
            ListNode* second = head->next;

            // Swap the pair
            prev->next = second;
            first->next = second->next;
            second->next = first;

            // Move pointers forward
            prev = first;
            head = first->next;
        }

        // Return the new head (after the dummy node)
        ListNode* newHead = dummy->next;
        delete dummy; // Free the dummy node to avoid memory leaks
        return newHead;
    }
    
};