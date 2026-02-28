// Last updated: 2/28/2026, 4:28:31 PM
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode p,q;

        if(head == null) return false;

        p = head;
        q = head.next;

        if(p == null || q == null) return false;

        while(q != null && q.next != null){
            if(p == q) return true;

            p = p.next;
            q = q.next.next;
        }

        return false;

    }
}