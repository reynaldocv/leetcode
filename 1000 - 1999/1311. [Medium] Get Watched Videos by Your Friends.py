# https://leetcode.com/problems/get-watched-videos-by-your-friends/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        stack = [id]
        seen = {id: True}
        lvl = 0
        
        while lvl < level: 
            newStack = []
            for person in stack: 
                for friend in friends[person]:
                    if friend not in seen: 
                        seen[friend] = True 
                        newStack.append(friend)
                        
            stack = newStack
            lvl += 1 
        
        counter = defaultdict(lambda: 0)
        videos = set()
        for friend in stack: 
            for video in watchedVideos[friend]:
                counter[video] += 1 
                videos.add(video)
                
        videos = list(videos)        
        videos.sort(key = lambda item: (counter[item], item))
        
        return videos
