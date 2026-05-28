# Last updated: 5/28/2026, 11:10:55 PM
1class Solution:
2    def reverseList(self, head):
3
4        if not head or not head.next:
5            return head
6
7        newHead = self.reverseList(head.next)
8
9        head.next.next = head
10
11        head.next = None
12
13        return newHead