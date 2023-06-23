# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(travel)
        
        for i in range(1, n):
            travel[i] += travel[i - 1]
            
        travel.insert(0, 0)
        
        last = defaultdict(lambda: 0)
        counter = defaultdict(lambda: 0)
        
        for (i, word) in enumerate(garbage):
            for char in word: 
                last[char] = i 
                
                counter[char] += 1 
                
        ans = 0 
        
        for char in last: 
            ans += travel[last[char]] + counter[char]
            
        return ans 
