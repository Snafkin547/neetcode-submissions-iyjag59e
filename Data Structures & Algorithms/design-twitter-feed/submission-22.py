# No need to consider deleting post
class Twitter:

    def __init__(self):
        # User: -Time and tweetId
        self.time = 0
        self.tweets = defaultdict(list)
        # User:followees relationship
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Post : (-time, tweetId)
        self.tweets[userId].append((-self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Return 10 most recent tweet Ids posted by this user and following users, ordered from most recent
        # Build a heapq return first/dont forget to add yourself
        self.following[userId].add(userId)
        minHeap = []
        res = []
        if len(self.following[userId]) >= 10:
            maxheap = []
            for fol in self.following[userId]:
                if fol in self.tweets:
                    index = len(self.tweets[fol]) - 1
                    time, tweetId = self.tweets[fol][index]
                    heapq.heappush(maxHeap, (-time, tweetId, fol, index - 1))
                    if max(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            # Construct return list
            while maxHeap:
                time, tweetId, fol, idx = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, (-time, tweetId, fol, idx))
        else:
            for fol in self.following[userId]:
                if fol in self.tweets:
                    index = len(self.tweets[fol]) - 1
                    time, tweetId = self.tweets[fol][index]
                    heapq.heappush(minHeap, (time, tweetId, fol, index - 1))    
        while minHeap and len(res) < 10:
            time, tweetId, fol, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweets[fol][idx]
                heapq.heappush(minHeap, (time, tweetId, fol, idx - 1))    
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
