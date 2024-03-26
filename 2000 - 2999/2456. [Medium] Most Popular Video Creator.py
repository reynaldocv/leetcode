# https://leetcode.com/problems/most-popular-video-creator/

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        popularity = defaultdict(lambda: 0)
        mostViewed = defaultdict(lambda: (inf, ""))
        
        mostViews = 0 
        
        for (ith, creator) in enumerate(creators):
            code = ids[ith]
            cnt = views[ith]
            
            popularity[creator] += cnt
            mostViewed[creator] = min(mostViewed[creator], (-cnt, code))
            
            mostViews = max(mostViews, popularity[creator])
            
        ans = []
        
        for key in popularity: 
            if popularity[key] == mostViews: 
                (_, code) = mostViewed[key]
                
                ans.append((key, code))
                
        return ans 
