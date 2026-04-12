# Last updated: 4/12/2026, 5:52:48 PM
1class Solution:
2    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
3        dummy = ListNode()
4        heap = []
5        
6        for i in range(len(lists)):
7            node = lists[i]
8            if node: heap.append((node.val, i, node))
9
10        heapify(heap)
11        
12        head = dummy
13        while heap:
14            _, i, node = heappop(heap)
15            head.next = node
16            head = node
17            if node.next:
18                heappush(heap, (node.next.val, i, node.next))
19                node.next = None
20        return dummy.next