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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // carry addition
        int carry = 0;
        ListNode * result = new ListNode();
        ListNode * head = result;
        while ((l1 != nullptr or l2 != nullptr) and result != nullptr) {
            int sum = 0;
            if (l1 != nullptr)
                sum += l1->val;
            if (l2 != nullptr)
                sum += l2->val;
                        
            result->val = (sum % 10 + carry) % 10;
            carry = (sum + carry) / 10;
            cout << carry << " " << result->val << endl;
            
            if ((l1 && l1->next != nullptr) or (l2 && l2->next != nullptr)) {
                result->next = new ListNode();
                result = result->next;
            }
            if (l1)
                l1 = l1->next;
            if (l2)
                l2 = l2->next;
        }
        if (carry > 0) {
            result->next = new ListNode(carry);
        } else
            result = nullptr;
        return head;
    }
};