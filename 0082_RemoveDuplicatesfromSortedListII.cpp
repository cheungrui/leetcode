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
        ListNode *first, *a, *b, *c, *temp;
        first = new ListNode(-1);
        a = first;
        first->next = head;
        b=a->next;
        while(b!=NULL){
            c=b->next;
            //c是空的
            if(c==NULL){
                return first->next;
            }
            //b这个结点值是独一无二的
            if(c->val!=b->val){
                a=b;
                b=c;
            }else{
                //将c的位置放在和b值相同的最后一个结点上
                while(c->next!=NULL && c->next->val==c->val){
                    c=c->next;
                }
                b=c->next;
                //用来删除重复结点的
                // c=a->next;
                // while(c!=b){
                //     temp =c;
                //     c = c->next;
                //     delete temp;
                // }
                a->next = b;
            }
        }
        return first->next;
    }
};