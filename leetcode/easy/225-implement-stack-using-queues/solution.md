# Implement Stack using Queues

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/implement-stack-using-queues/submissions/1956001439/
- **Date:** 2026-03-22

## Solution

```java
import java.util.*;

class MyStack {
    Queue<Integer> q;

    public MyStack() {
        this.q = new LinkedList<>();
    }

    public void push(int x) {
        int s = q.size();
        q.add(x);

        for (int i = 0; i < s; i++) {
            q.add(q.poll());
        }
    }

    public int pop() {
        int n = q.peek();
        q.poll();
        return n;
    }

    public int top() {
        return q.peek();
    }

    public boolean empty() {
        return q.isEmpty();
    }
}

```

---
*Generated automatically by LeetFeedback Extension*
