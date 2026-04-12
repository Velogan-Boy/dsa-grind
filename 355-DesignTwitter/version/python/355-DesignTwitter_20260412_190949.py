# Last updated: 4/12/2026, 7:09:49 PM
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
19
20        if userId in self.user_follows:
21            for followeeId in self.user_follows[userId]:
22                if followeeId in self.user_tweets:
23                    heap.extend(self.user_tweets[followeeId][-10:])
24                    
25        heapq.heapify(heap)
26        feed = []
27        while heap and len(feed) < 10:
28            feed.append(heapq.heappop(heap)[1])
29        return feed
30    
31    def follow(self, followerId, followeeId):
32        if followerId not in self.user_follows:
33            self.user_follows[followerId] = set()
34        if followerId != followeeId:
35            self.user_follows[followerId].add(followeeId)
36    
37    def unfollow(self, followerId, followeeId):
38        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
39            self.user_follows[followerId].remove(followeeId)