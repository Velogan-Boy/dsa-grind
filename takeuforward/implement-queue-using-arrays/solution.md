# Implement Queue using Arrays

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/implement-queue-using-arrays
- **Date:** 2026-03-22

## Solution

```java
class ArrayQueue {
    private int capacity;
    private int rear;
    private int front;
    private int[] queue;

    public ArrayQueue(int capacity){
        this.capacity = capacity;
        this.queue = new int[capacity];
        this.front = -1;
        this.rear = -1;
    }

    public ArrayQueue() {
        this(1000);
    }

    public void push(int x) {
        if (front == capacity - 1) {
            System.out.println("Queue is full");
            return;
        }

        if (rear == -1) rear = 0;

        queue[++front] = x;
    }

    public int pop() {
        if (rear == -1 || rear > front) {
            return -1;
        }

        int val = queue[rear++];

        if (rear > front) {
            rear = front = -1;
        }

        return val;
    }

    public int peek() {
        if (rear == -1 || rear > front) return -1;
        return queue[rear];
    }

    public boolean isEmpty() {
        return rear == -1;
    }
}
```

---
*Generated automatically by LeetFeedback Extension*
