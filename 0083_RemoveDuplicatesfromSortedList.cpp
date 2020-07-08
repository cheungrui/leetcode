/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL){return head;}
        ListNode *a, *b, *temp;
        a = head;
        while(a!=NULL && a->next!=NULL){
            b = a->next;
            if(a->val==b->val){
                a->next=b->next;
                //注释部分是用来删除空间的
                // delete b;
            }else{
                a=b;
            }
        }
        return head;
    }
};