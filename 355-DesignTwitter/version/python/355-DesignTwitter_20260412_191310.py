# Last updated: 4/12/2026, 7:13:10 PM
1import heapq
2
3class Twitter(object):
4    def __init__(self):
5        self.timestamp = 0
6        self.user_tweets = defaultdict(list)
7        self.user_follows = defaultdict(set)
8    
9    def postTweet(self, userId, tweetId):
10        self.timestamp += 1
11        self.user_tweets[userId].append((-self.timestamp, tweetId))
12    
13    def getNewsFeed(self, userId):
14        heap = []
15
16        if userId in self.user_tweets:
17            heap.extend(self.user_tweets[userId][-10:])
18
19        if userId in self.user_follows:
20            for followeeId in self.user_follows[userId]:
21                if followeeId in self.user_tweets:
22                    heap.extend(self.user_tweets[followeeId][-10:])
23                    
24
25        heapq.heapify(heap)
26        feed = []
27
28        while heap and len(feed) < 10:
29            feed.append(heapq.heappop(heap)[1])
30        return feed
31    
32    def follow(self, followerId, followeeId):
33        if followerId != followeeId:
34            self.user_follows[followerId].add(followeeId)
35    
36    def unfollow(self, followerId, followeeId):
37        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
38            self.user_follows[followerId].remove(followeeId)