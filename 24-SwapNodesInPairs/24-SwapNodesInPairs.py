# Last updated: 7/12/2026, 6:25:24 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            nxtPair = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = nxtPair
            prev.next = second

            prev = curr
            curr = nxtPair

        return dummy.next
