# Last updated: 7/12/2026, 6:25:26 PM
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr