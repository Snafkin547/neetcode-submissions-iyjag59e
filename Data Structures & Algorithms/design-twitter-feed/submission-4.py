import heapq
class Twitter:

    def __init__(self):
        self.cnt = 0
        self.userMap = defaultdict(set) # userid -> set(followee ids)
        self.tweetMap = defaultdict(list) # userid -> [time, poster, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.cnt, tweetId])
        self.cnt -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get followees
        followees = self.userMap[userId].copy()
        followees.add(userId)

        # make a heap of tweets with next index for each poster
        minHeap = []
        for followee in followees:
            if followee in self.tweetMap and self.tweetMap[followee]:
                idx = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][idx]
                heapq.heappush(minHeap, [time, followee, tweetId, idx - 1])
        
        # iterate over the heap of tweets
        res = []
        while minHeap and len(res) < 10:
            time, poster, tweetId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweetMap[poster][idx]
                heapq.heappush(minHeap, [time, poster, tweetId, idx - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].discard(followeeId)
