# Implement Stack using Arrays

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/implement-stack-using-arrays
- **Date:** 2026-03-22

## Solution

```java
class ArrayStack {
    private List<Integer> stack;

    public ArrayStack() {
        this.stack = new ArrayList<>();
    }

    public void push(int x) {
       this.stack.add(x);
    }

    public int pop() {
      return this.stack.remove(this.stack.size() - 1);
    }

    public int top() {
        return this.stack.get(this.stack.size() - 1);
    }

    public boolean isEmpty() {
        return this.stack.isEmpty();
    }
}

```

---
*Generated automatically by LeetFeedback Extension*
