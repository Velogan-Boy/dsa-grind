# Last updated: 4/12/2026, 7:06:58 PM
1import heapq
2
3class Twitter(object):
4    def __init__(self):
5        self.timestamp = 0
6        self.user_tweets = {}
7        self.user_follows = {}
8    
9    def postTweet(self, userId, tweetId):
10        if userId not in self.user_tweets:
11            self.user_tweets[userId] = []
12        self.timestamp += 1
13        self.user_tweets[userId].append((-self.timestamp, tweetId))
14    
15    def getNewsFeed(self, userId):
16        heap = []
17        if userId in self.user_tweets:
18            heap.extend(self.user_tweets[userId][-10:])
19        if userId in self.user_follows:
20            for followeeId in self.user_follows[userId]:
21                if followeeId in self.user_tweets:
22                    heap.extend(self.user_tweets[followeeId][-10:])
23        heapq.heapify(heap)
24        feed = []
25        while heap and len(feed) < 10:
26            feed.append(heapq.heappop(heap)[1])
27        return feed
28    
29    def follow(self, followerId, followeeId):
30        if followerId not in self.user_follows:
31            self.user_follows[followerId] = set()
32        if followerId != followeeId:
33            self.user_follows[followerId].add(followeeId)
34    
35    def unfollow(self, followerId, followeeId):
36        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
37            self.user_follows[followerId].remove(followeeId)