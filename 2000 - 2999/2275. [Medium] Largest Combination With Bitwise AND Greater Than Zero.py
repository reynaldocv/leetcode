# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in candidates: 
            idx = 0 
            
            while num: 
                bit = num % 2
                
                if bit == 1: 
                    counter[idx] += 1 
                    
                num //= 2                 
                idx += 1 
                
        ans = 0 
        
        for key in counter: 
            ans = max(ans, counter[key])
            
        return ans 
                
            
        
        
        
