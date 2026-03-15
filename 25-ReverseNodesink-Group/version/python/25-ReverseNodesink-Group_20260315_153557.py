# Last updated: 3/15/2026, 3:35:57 PM
1class Solution:
2    def reverseKGroup(self, head, k):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        groupPrev = dummy
7
8        while True:
9            kth = self.getKthNode(groupPrev, k)
10            if not kth:
11                break
12
13            groupNext = kth.next
14
15            prev = groupNext
16            curr = groupPrev.next
17
18            for _ in range(k):
19                temp = curr.next
20                curr.next = prev
21                prev = curr
22                curr = temp
23
24            temp = groupPrev.next
25            groupPrev.next = kth
26            groupPrev = temp
27
28        return dummy.next
29
30    def getKthNode(self, curr, k):
31        while curr and k > 0:
32            curr = curr.next
33            k -= 1
34        return curr