# Last updated: 7/12/2026, 10:18:15 PM
1class Solution:
2    def fizzBuzz(self, n: int) -> List[str]:
3
4        answer = [""] * n
5
6        for i in range(1,n + 1):
7            if i % 3 == 0:
8                answer[i - 1] += "Fizz"
9            
10            if i % 5 == 0:
11                answer[i - 1] += "Buzz"
12
13            if i % 3 != 0 and i % 5 != 0:
14                answer[i - 1] += str(i)
15
16        return answer
17            
18
19            
20
21        