# Last updated: 3/15/2026, 4:25:20 PM
1# class ListNode:
2#     def __init__(self, val=0, next=None, random=None):
3#         self.val = val
4#         self.next = next
5#         self.random = random
6
7class Solution:
8    def insertCopyInBetween(self, head):
9        temp = head
10        while temp:
11            nextElement = temp.next
12            copy = ListNode(temp.val)
13            
14            copy.next = nextElement
15            temp.next = copy
16            temp = nextElement
17
18    def connectRandomPointers(self, head):
19        temp = head
20        while temp:
21            copyNode = temp.next
22            
23            if temp.random:
24                copyNode.random = temp.random.next
25            else:
26                copyNode.random = None
27            
28            temp = temp.next.next
29
30    def getDeepCopyList(self, head):
31        temp = head
32        dummyNode = ListNode(-1)
33        res = dummyNode
34
35        while temp:
36            res.next = temp.next
37            res = res.next
38
39            temp.next = temp.next.next
40            temp = temp.next
41        
42        return dummyNode.next
43
44    def copyRandomList(self, head):
45        if not head: return None
46
47        self.insertCopyInBetween(head)
48        self.connectRandomPointers(head)
49        return self.getDeepCopyList(head)
50
51