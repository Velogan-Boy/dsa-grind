# Swap Two Numbers

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/swap-two-numbers
- **Date:** 2026-03-21

## Solution

```python
class Solution:
    def swap(self, a, b):
        """
        Swap two integers and return them.

        Args:
            a (int): First integer.
            b (int): Second integer.

        Returns:
            Tuple[int, int]: The two integers, swapped.
        """

        a = a ^ b
        b = a ^ b   
        a = a ^ b

        return (a, b)

```

---
*Generated automatically by LeetFeedback Extension*
