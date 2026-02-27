// Last updated: 2/27/2026, 5:12:03 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {

        if(head == null || head.next == null) return head;

        ListNode q,r;
        q = head;
        r = head.next;

        while(q != null && r != null){

            if(q.val == r.val){
                // remove r
                q.next = r.next;
                r = r.next;
                continue;

            }
            q = r;
            if(r != null) r = r.next;
        }

        return head;
        
    }
}