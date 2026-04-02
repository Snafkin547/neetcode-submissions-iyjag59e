class minHeap:
    def __init__(self):
        self.heap = []

    def push(self, val:Any) -> None:
        self.heap.append(val)
        self.bubble_up(len(self.heap) - 1)

    def pop(self) -> Any:
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return root

    def bubble_down(self, idx:int) -> None:
        n = len(self.heap)
        while True:
            smallest = idx
            l = idx * 2 + 1
            r = idx * 2 + 2
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest != idx:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break

    def bubble_up(self, idx:int) -> None:
        while idx > 0:
            parent = (idx - 1) //2
            if self.heap[parent] > self.heap[idx]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def peek(self) -> Any:
        return self.heap[0] if self.heap else None


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
        mh = minHeap()
        umap_copy = self.userMap[userId].copy()
        umap_copy.add(userId)
        # if len(self.userMap[userId]) >= 10:
        for followeeId in umap_copy:
            if followeeId in self.tweetMap: # Add just the latest tweet of the poster
                idx = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][idx]
                mh.push([time, tweetId, followeeId, idx - 1])
                if len(mh.heap) > 10:
                    mh.pop()
        # Traverse the Heap
        res = []
        while mh.heap and len(res) < 10:
            time, tweetId, followeeId, idx = mh.pop()
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweetMap[followeeId][idx]
                mh.push([time, tweetId, followeeId, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].discard(followeeId)
        
