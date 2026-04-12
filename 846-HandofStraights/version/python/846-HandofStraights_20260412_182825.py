# Last updated: 4/12/2026, 6:28:25 PM
1class Solution:
2    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
3        if len(hand) % groupSize != 0:
4            return False
5
6        count = Counter(hand)
7        hand.sort()
8
9        for card in hand:
10            if count[card] == 0:
11                continue
12
13            for i in range(groupSize):
14                if count[card + i] == 0:
15                    return False
16                count[card + i] -= 1
17
18        return True