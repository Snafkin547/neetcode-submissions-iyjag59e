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
        followees = self.following[userId]
        followees.add(userId)
        minHeap = []
        for fol in followees:
            for post in self.tweets[fol]:
                heapq.heappush(minHeap, post) # Post : (-time, tweetId)
        res = []
        # Construct return list
        for _ in range(min(10, len(minHeap))):
            time, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
