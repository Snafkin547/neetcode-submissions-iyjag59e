import datetime;
import heapq
class User:
    def __init__(self, userId):
        self.userId = userId
        self.following = set()
    
    def isFollowing(self, following):
        return following in self.following or following == self.userId
    
    def follow(self, following) -> None:
        self.following.add(following)

    def unfollow(self, unfollowing) -> None:
        self.following.discard(unfollowing)

class Twitter:

    def __init__(self):
        self.users = {}
        self.latestTweet = []
        self.time = 0
    
    def getUser(self, userId: int) -> User:
        if userId not in self.users:
            self.users[userId] = User(userId)
        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        heapq.heappush(self.latestTweet, (self.time, userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
         Fetches at most the 10 most recent tweet IDs in the user's news feed. 
         Each item must be posted by users who the user is following or by the user themself. 
         Tweets IDs should be ordered from most recent to least recent.
        - heapq for relevant tweets
        - keep popping till 10/len(minHeap)
        '''
        res = []
        reserve = []
        
        cnt = 10
        currUser = self.getUser(userId)
        while self.latestTweet and cnt > 0:
            time, poster, tweetId = heapq.heappop(self.latestTweet)
            reserve.append((time, poster, tweetId))

            if currUser.isFollowing(poster):
                res.append(tweetId)
                cnt -= 1
            else:
                continue
        for r in reserve:
            heapq.heappush(self.latestTweet, r)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        currUser = self.getUser(followerId)
        currUser.follow(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        currUser = self.getUser(followerId)
        currUser.unfollow(followeeId)        
