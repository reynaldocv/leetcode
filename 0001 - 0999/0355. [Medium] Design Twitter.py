# https://leetcode.com/problems/design-twitter/

class User: 
    def __init__(self):
        self.followers = set()
        self.following = set()

class Twitter:

    def __init__(self):
        self.users = defaultdict(User)
        self.tweets = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([tweetId, userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        
        for i in range(len(self.tweets) -1, -1, -1):
            if len(ans) == 10:
                break
            (_tweetId, _userId) = self.tweets[i]
            if _userId in self.users[userId].following or _userId == userId:
                ans.append(_tweetId)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followeeId].followers.add(followerId)
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users[followeeId].followers: 
            self.users[followeeId].followers.remove(followerId)
        if followeeId in self.users[followerId].following: 
            self.users[followerId].following.remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
