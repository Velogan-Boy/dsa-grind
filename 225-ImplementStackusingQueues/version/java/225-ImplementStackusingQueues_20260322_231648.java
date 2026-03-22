// Last updated: 3/22/2026, 11:16:48 PM
1import java.util.*;
2
3class MyStack {
4    Queue<Integer> q;
5
6    public MyStack() {
7        this.q = new LinkedList<>();
8    }
9
10    public void push(int x) {
11        int s = q.size();
12        q.add(x);
13
14        for (int i = 0; i < s; i++) {
15            q.add(q.poll());
16        }
17    }
18
19    public int pop() {
20        int n = q.peek();
21        q.poll();
22        return n;
23    }
24
25    public int top() {
26        return q.peek();
27    }
28
29    public boolean empty() {
30        return q.isEmpty();
31    }
32}
33