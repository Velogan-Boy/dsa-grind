# Last updated: 4/12/2026, 7:06:02 PM
1class Twitter:
2    def __init__(self):
3        self.count = 0
4        self.tweetMap = defaultdict(list)  
5        self.followMap = defaultdict(set)  
6
7    def postTweet(self, userId: int, tweetId: int) -> None:
8        self.tweetMap[userId].append([self.count, tweetId])
9        self.count -= 1
10
11    def getNewsFeed(self, userId: int) -> List[int]:
12        res = []
13        minHeap = []
14
15        self.followMap[userId].add(userId)
16        for followeeId in self.followMap[userId]:
17            if followeeId in self.tweetMap:
18                index = len(self.tweetMap[followeeId]) - 1
19                count, tweetId = self.tweetMap[followeeId][index]
20                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
21
22        while minHeap and len(res) < 10:
23            count, tweetId, followeeId, index = heapq.heappop(minHeap)
24            res.append(tweetId)
25            if index >= 0:
26                count, tweetId = self.tweetMap[followeeId][index]
27                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
28        return res
29
30    def follow(self, followerId: int, followeeId: int) -> None:
31        self.followMap[followerId].add(followeeId)
32
33    def unfollow(self, followerId: int, followeeId: int) -> None:
34        if followeeId in self.followMap[followerId]:
35            self.followMap[followerId].remove(followeeId)
36