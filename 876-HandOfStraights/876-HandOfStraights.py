# Last updated: 7/12/2026, 6:18:07 PM
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
            if len(hand) % groupSize != 0:
                return False

            count = Counter(hand)
            heap = list(count.keys())
            heapq.heapify(heap)

            while heap:
                first = heap[0]

                for i in range(groupSize):
                    if count[first + i] == 0:
                        return False

                    count[first + i] -= 1

                    if count[first + i] == 0:
                        if first + i != heap[0]:
                            return False
                        heapq.heappop(heap)

            return True