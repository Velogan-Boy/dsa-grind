# Implement stack using Linkedlist

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/implement-stack-using-linkedlist
- **Date:** 2026-03-22

## Solution

```java
import java.util.*;

class Node {
    int val;
    Node next;
    Node(int d) {
        val = d;
        next = null;
    }
}

class LinkedListStack {
    private Node head; 
    private int size;

    public LinkedListStack() {
        head = null;
        size = 0;
    }

    public void push(int x) {
        Node element = new Node(x);
        
        element.next = head;
        head = element; 
        
        size++;
    }

    public int pop() {
        if (head == null) {
            return -1; 
        }
        
        int value = head.val;
        Node temp = head; 
        head = head.next; 
        temp = null;
        size--; 
        
        return value; 
    }

    public int top() {
        if (head == null) {
            return -1; 
        }
        
        return head.val; 
    }

    public boolean isEmpty() {
        return (size == 0);
    }
}

```

---
*Generated automatically by LeetFeedback Extension*
