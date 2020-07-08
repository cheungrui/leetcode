/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

 /*
 本题是说将一串链表顺时针旋转k个，
*/
func rotateRight(head *ListNode, k int) *ListNode {
    if k == 0 || head==nil {
        return head
    }
    var ptr1, ptr2 *ListNode = head, head
    // var ptr2 *ListNode = head
    var i int = 0
    // first try to find the diff node length
    for ; i < k; i ++ {
        if ptr1.Next == nil {
            break
        } else {
            ptr1 = ptr1.Next
        }
    }

    // the k is to big, i+1 is the length of the list node
    if i < k {
        i = k % (i + 1)
        return rotateRight(head, i)
    }

    // to move to the tail
    for {
        if ptr1.Next == nil {
            break
        } else {
            ptr1 = ptr1.Next
            ptr2 = ptr2.Next
        }
    }

    //do split
    ptr1.Next = head
    head = ptr2.Next
    ptr2.Next = nil
    return head
}