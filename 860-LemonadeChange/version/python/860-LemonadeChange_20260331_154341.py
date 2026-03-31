# Last updated: 3/31/2026, 3:43:41 PM
1class Solution:
2    def lemonadeChange(self, bills: List[int]) -> bool:
3        five = 0
4        ten = 0
5
6        for i in range(len(bills)):
7            if bills[i] == 5:
8                five += 1
9            elif bills[i] == 10:
10                if five > 0:
11                    five -= 1
12                    ten += 1
13                else:
14                    return False
15            elif bills[i] == 20:
16                if five > 0 and ten > 0:
17                    five -= 1
18                    ten -= 1
19                elif five >= 3:
20                    five -= 3
21                else:
22                    return False
23                    
24        return True