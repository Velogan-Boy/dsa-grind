# Last updated: 5/20/2026, 9:57:21 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reorderList(self, head: Optional[ListNode]) -> None:
9
10        def copyList(head):
11            dummy = ListNode()
12            curr = dummy
13            p = head
14
15            while p:
16                curr.next = ListNode(p.val)
17                curr = curr.next
18                p = p.next
19
20            return dummy.next
21
22        def reverseList(head):
23            if not head or not head.next:
24                return head
25
26            prev = None
27            curr = head
28
29            while curr:
30                temp = curr.next
31                curr.next = prev
32                prev = curr
33                curr = temp
34
35            return prev
36
37        if not head or not head.next:
38            return
39
40        list1 = head
41        list2 = reverseList(copyList(head))
42
43        # Count original nodes
44        n = 0
45        p = head
46        while p:
47            n += 1
48            p = p.next
49
50        dummy = ListNode()
51        tail = dummy
52        used = 0
53
54        while used < n:
55            tail.next = list1
56            tail = tail.next
57            list1 = list1.next
58            used += 1
59
60            if used == n:
61                break
62
63            tail.next = list2
64            tail = tail.next
65            list2 = list2.next
66            used += 1
67
68        tail.next = None
69
70        head.val = dummy.next.val
71        head.next = dummy.next.next