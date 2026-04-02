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
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Return 10 most recent tweet Ids posted by this user and following users, ordered from most recent
        # Build a heapq return first/dont forget to add yourself
        self.following[userId].add(userId)
        minHeap = []
        for fol in self.following[userId]:
            if fol in self.tweets:
                index = len(self.tweets[fol]) - 1
                time, tweetId = self.tweets[fol][index]
                heapq.heappush(minHeap, (time, tweetId, fol, index - 1))
        res = []
        # Construct return list
        while len(res) < 10 and minHeap:
            time, tweetId, fol, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweets[fol][idx]
                heapq.heappush(minHeap, (time, tweetId, fol, idx-1))
        # self.following[userId].discard(userId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
