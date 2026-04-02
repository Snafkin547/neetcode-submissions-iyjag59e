import heapq
class Twitter:

    def __init__(self):
       self.tweetMap = defaultdict(list) # userId -> [[time, tweetId]]
       self.userMap = defaultdict(set) # userId -> [followeeIds]
       self.time = 0 # Keep track of the order of tweets (Use negative to have recent)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId]) # Revisit
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Make a Heap with index for each poster
        minHeap = []
        umap_copy = self.userMap[userId].copy()
        umap_copy.add(userId)
        for followeeId in umap_copy:
            if followeeId in self.tweetMap: # Add just the latest tweet of the poster
                idx = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [time, tweetId, followeeId, idx - 1])
        # Traverse the Heap
        res = []
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [time, tweetId, followeeId, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].discard(followeeId)
        
