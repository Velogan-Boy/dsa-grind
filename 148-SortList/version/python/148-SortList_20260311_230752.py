# Last updated: 3/11/2026, 11:07:52 PM
1class Solution:
2    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
3        if head is None or head.next is None:
4            return head
5        
6        middle = self.findMiddle(head)
7        
8        right = middle.next
9        middle.next = None
10        left = head
11        
12        left = self.sortList(left)
13        right = self.sortList(right)
14        
15        return self.mergeTwoSortedLinkedLists(left, right)
16
17
18    def mergeTwoSortedLinkedLists(self, list1, list2):
19        dummyNode = ListNode(-1)
20        temp = dummyNode
21
22        while list1 is not None and list2 is not None:
23            if list1.val <= list2.val:
24                temp.next = list1
25                list1 = list1.next
26            else:
27                temp.next = list2
28                list2 = list2.next
29                
30            temp = temp.next
31
32        if list1 is not None:
33            temp.next = list1
34        else:
35            temp.next = list2
36
37        return dummyNode.next
38
39    def findMiddle(self, head):
40        if head is None or head.next is None:
41            return head
42
43        slow = head
44        fast = head.next
45
46        while fast is not None and fast.next is not None:
47            slow = slow.next
48            fast = fast.next.next
49
50        return slow
51
52      
53