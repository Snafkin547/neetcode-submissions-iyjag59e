class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        curr = []
        self.followers[userId].add(userId)
        
        for follower in self.followers[userId]:
            if follower in self.tweets:
                idx = len(self.tweets[follower]) - 1
                t, tweetid = self.tweets[follower][idx]
                heapq.heappush(curr, (t, tweetid, follower, idx - 1))

        while len(res) < 10 and curr:
            t, tweetid, follower, idx = heapq.heappop(curr)
            res.append(tweetid)

            if idx >= 0:
                t, tweetid = self.tweets[follower][idx]
                heapq.heappush(curr, (t, tweetid, follower, idx - 1))
                                    
        self.followers[userId].remove(userId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)
        
