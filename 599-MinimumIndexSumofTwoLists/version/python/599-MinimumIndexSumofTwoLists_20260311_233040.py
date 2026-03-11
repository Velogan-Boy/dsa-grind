# Last updated: 3/11/2026, 11:30:40 PM
1class Solution:
2    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
3        count = {}
4        for i in range(len(list1)):
5            for j in range(len(list2)):
6                if list1[i] == list2[j]:
7                    indexsum = i + j
8                    count[list1[i]] = indexsum
9        min_indexsum = min(count.values())
10        ans = []
11        for key,val in count.items():
12            if val == min_indexsum:
13                ans.append(key)
14        return ans