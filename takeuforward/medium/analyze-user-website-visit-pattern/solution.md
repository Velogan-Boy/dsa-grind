# 339. Analyze User Website Visit Pattern

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Medium
- **URL:** https://takeuforward.org/practice/dsa/analyze-user-website-visit-pattern
- **Date:** 2026-10-13

## Solution

```python
from collections import defaultdict

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        n = len(username)

        activity = [(timestamp[i], username[i], website[i]) for i in range(n)]

        activity.sort(key=lambda x: (x[1], x[0]))

        hashMap = defaultdict(int)

        i = 0
        while i < n:
            j = i
            while j < n and activity[j][1] == activity[i][1]:
                j += 1

            seen = set()

            for a in range(i, j):
                for b in range(a + 1, j):
                    for c in range(b + 1, j):
                        pattern = (
                            activity[a][2],
                            activity[b][2],
                            activity[c][2]
                        )
                        if pattern not in seen:
                            seen.add(pattern)
                            hashMap[pattern] += 1

            i = j

        maxi = 0
        ans = None

        for key, value in hashMap.items():
            if value > maxi or (value == maxi and (ans is None or key < ans)):
                maxi = value
                ans = key

        return list(ans)
```

---
*Generated automatically by LeetFeedback Extension*
