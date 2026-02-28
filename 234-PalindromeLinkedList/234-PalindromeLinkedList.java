// Last updated: 2/28/2026, 4:27:49 PM
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
    public boolean isPalindrome(ListNode head) {

        ListNode fast = head;
        ListNode slow = head;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode rev_head = reverse(slow);

        while(head != null && rev_head != null){
            if(head.val != rev_head.val) return false;

            head = head.next;
            rev_head = rev_head.next;
        }

        return true;
        
    }

    public static ListNode reverse(ListNode head){
        ListNode p = null;
        ListNode q = null;
        ListNode r = head;

        while(r != null){
            p = q;
            q = r;
            r = r.next;
            q.next = p;
        }

        return q;
    }
}