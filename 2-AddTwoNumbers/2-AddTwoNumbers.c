// Last updated: 2/27/2026, 5:24:09 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    
    struct ListNode *l3 = NULL, *head = NULL;
    int carry = 0;
    int flag = 0;
    
    l3 = (struct ListNode*) malloc(sizeof(struct ListNode));
    
               
    while(l1 || l2 || carry != 0) {
        struct ListNode *temp;
        temp = (struct ListNode*) malloc(sizeof(struct ListNode));
        
                         
        if(l1 && l2){
            temp->val = (l1->val + l2->val + carry) % 10;
            carry = (l1->val + l2->val + carry) / 10;
            l1 = l1->next;
            l2 = l2->next;
        }else if(!l1 && !l2){
            if( carry != 0){
                temp->val = carry;
                temp->next = NULL;
                carry = 0;
            } else break;
        
        }else if(!l2){
            temp->val = (l1->val + carry) % 10;
            carry = (l1->val + carry) / 10;
            l1 = l1->next;
        }else if(!l1){
            temp->val = (l2->val + carry) % 10;
            carry = (l2->val + carry) / 10;
            l2 = l2->next;
        }
        
        if(flag == 0){
            l3 = temp;
            l3->next = NULL;
            head = l3;
            flag = 1;
            continue;
        }
        
        l3 -> next = temp;
        l3 = l3 -> next;
        if(l3){
        l3->next = NULL;
        }
    }
    
    
    return head;

}