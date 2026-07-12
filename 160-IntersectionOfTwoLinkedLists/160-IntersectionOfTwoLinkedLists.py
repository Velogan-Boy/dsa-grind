# Last updated: 7/12/2026, 6:21:54 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if headA is None or headB is None:
            return None

        d1, d2 = headA, headB

        while d1 != d2:
            d1 = d1.next
            d2 = d2.next

            if d1 == d2:
                return d1

            if d1 is None:
                d1 = headB
            if d2 is None:
                d2 = headA

        return d1

        