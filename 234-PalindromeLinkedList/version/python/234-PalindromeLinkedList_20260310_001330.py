# Last updated: 3/10/2026, 12:13:30 AM
1class Solution:
2    def isPalindrome(self, head: ListNode) -> bool:
3        fast = head
4        slow = head
5        
6        while fast and fast.next:
7            fast = fast.next.next
8            slow = slow.next
9            
10        prev = None
11        while slow:
12            tmp = slow.next
13            slow.next = prev
14            prev = slow
15            slow = tmp
16        
17        left, right = head, prev
18
19        while right:
20            if left.val != right.val:
21                return False
22                
23            left = left.next
24            right = right.next
25
26        return True
27