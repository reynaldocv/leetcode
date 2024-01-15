# https://leetcode.com/problems/design-twitter/submissions/

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(lambda: [])                
        self.count = defaultdict(lambda: 0)
        
        self.cnt = 1 
        
        self.following = defaultdict(lambda: set())
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].insert(0, tweetId)
        
        self.count[tweetId] = self.cnt
        
        self.cnt += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        tmp = []
        tmp.extend(self.tweets[userId][: 10])
        
        for followee in self.following[userId]:
            tmp.extend(self.tweets[followee])
            
        tmp.sort(key = lambda item: -self.count[item])
        
        return tmp[: 10]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
