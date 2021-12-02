# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = {}
        for t in time: 
            counter[t % 60] = counter.get(t % 60, 0) + 1
        
        ans = 0
        for t in counter:
            if t <= 30:
                if t == 0 or t == 30: 
                    ans += counter[t]*(counter[t] - 1)//2
                elif 60 - t in counter: 
                    ans += counter[t] * counter[60 - t]
        
        return ans
            
        
