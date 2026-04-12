# Hand of Straights

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/hand-of-straights/submissions/1976404334/
- **Date:** 2026-04-12

## Solution

```python
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        hand.sort()

        for card in hand:
            if count[card] == 0:
                continue

            for i in range(groupSize):
                if count[card + i] == 0:
                    return False
                count[card + i] -= 1

        return True
```

---
*Generated automatically by LeetFeedback Extension*
