// Last updated: 3/22/2026, 11:44:25 PM
1class MyQueue {
2    Stack<Integer> queue;
3
4    public MyQueue() {
5        queue = new Stack<Integer>();
6    }
7
8    public void push(int x) {
9        Stack<Integer> tempStack = new Stack<>();
10
11        while (!queue.isEmpty()) {
12            tempStack.push(queue.pop());
13        }
14
15        queue.push(x);
16
17        while (!tempStack.isEmpty()) {
18            queue.push(tempStack.pop());
19        }
20    }
21
22    public int pop() {
23         if (!queue.isEmpty()) {
24            return queue.pop();
25        }
26        return -1;
27
28    }
29
30    public int peek() {
31        if (!queue.isEmpty()) {
32            return queue.peek();
33        }
34        return -1;
35    }
36
37    public boolean empty() {
38        return queue.isEmpty();
39    }
40}
41
42/**
43 * Your MyQueue object will be instantiated and called as such:
44 * MyQueue obj = new MyQueue();
45 * obj.push(x);
46 * int param_2 = obj.pop();
47 * int param_3 = obj.peek();
48 * boolean param_4 = obj.empty();
49 */