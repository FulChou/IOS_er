//https://leetcode.com/problems/add-two-numbers/

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
        ListNode* head  = new ListNode;
        ListNode *p = l1,*q = l2, *r = head ;
        int carry = 0;
        
        while(p || q){
            int sum = carry;
            if(p){
                sum+=p->val;
                p = p->next;
            }
            if(q){
                sum += q->val;
                q = q->next;
            }
            carry = sum/10;
            head->next = new ListNode(sum %10); // 空间耗费比较大。
            head = head->next;
            
        }
        if(carry>0){
            head->next = new ListNode(1);
        }
        return r->next;
    }
    
};
