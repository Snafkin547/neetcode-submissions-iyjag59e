import heapq
class Twitter:

    def __init__(self):
       self.tweetMap = defaultdict(list) # userId -> [[time, tweetId]]
       self.userMap = defaultdict(set) # userId -> [followeeIds]
       self.time = 0 # Keep track of the order of tweets (Use negative to have recent)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId]) # Revisit
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Make a Heap with index for each poster
        minHeap = []
        umap_copy = self.userMap[userId].copy()
        umap_copy.add(userId)
        for followeeId in umap_copy:
            for time, tweetId in self.tweetMap[followeeId]:
                heapq.heappush(minHeap, [time, tweetId])
        # Traverse the Heap
        res = []
        while minHeap and len(res) < 10:
            time, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].discard(followeeId)
        
