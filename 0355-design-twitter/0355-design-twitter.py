import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        heap = []
        self.following[userId].add(userId)
        
        for user in self.following[userId]:
            if self.tweets[user]:
                time, tweetId = self.tweets[user][-1]
                heap.append((-time, tweetId, user, len(self.tweets[user]) - 1))
        
        heapq.heapify(heap)
        res = []
        
        while heap and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:
                t, tid = self.tweets[user][idx - 1]
                heapq.heappush(heap, (-t, tid, user, idx - 1))
        
        return res

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)