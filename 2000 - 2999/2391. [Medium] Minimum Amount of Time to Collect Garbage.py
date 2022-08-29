# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        times = [0]
        
        for time in travel: 
            times.append(times[-1] + time)
            
        last = defaultdict(lambda: 0)
        
        ans = 0 
        
        for (i, word) in enumerate(garbage):
            for char in word: 
                ans += times[i] - last[char] + 1               
                last[char] = times[i]
            
        return ans 
