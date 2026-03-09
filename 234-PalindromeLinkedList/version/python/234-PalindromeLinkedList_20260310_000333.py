# Last updated: 3/10/2026, 12:03:33 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def isPalindrome(self, head: Optional[ListNode]) -> bool:
8        stack = []
9        
10        temp = head
11        
12        while temp:
13            stack.append(temp.val)
14            temp = temp.next
15        
16        temp = head
17        
18        while temp:
19            if temp.val != stack.pop():
20                return False
21            
22            temp = temp.next
23        
24        return True
25        