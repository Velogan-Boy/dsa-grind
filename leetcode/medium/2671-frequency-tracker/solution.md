# Frequency Tracker

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/frequency-tracker/submissions/1973288162/
- **Date:** 2026-04-09

## Solution

```python
class FrequencyTracker:
    def __init__(self):
        self.count = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[self.count[number]] -= 1
        self.count[number] += 1
        self.freq[self.count[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.count[number] > 0:
            self.freq[self.count[number]] -= 1
            self.count[number] -= 1
            self.freq[self.count[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


```

---
*Generated automatically by LeetFeedback Extension*
