# Implement Queue using Stacks

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/implement-queue-using-stacks/submissions/1956028422/
- **Date:** 2026-03-22

## Solution

```java
class MyQueue {
    Stack<Integer> queue;

    public MyQueue() {
        queue = new Stack<Integer>();
    }

    public void push(int x) {
        Stack<Integer> tempStack = new Stack<>();

        while (!queue.isEmpty()) {
            tempStack.push(queue.pop());
        }

        queue.push(x);

        while (!tempStack.isEmpty()) {
            queue.push(tempStack.pop());
        }
    }

    public int pop() {
         if (!queue.isEmpty()) {
            return queue.pop();
        }
        return -1;

    }

    public int peek() {
        if (!queue.isEmpty()) {
            return queue.peek();
        }
        return -1;
    }

    public boolean empty() {
        return queue.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
```

---
*Generated automatically by LeetFeedback Extension*
