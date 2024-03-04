# https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens) 
        
        tokens.sort() 
        
        start = 0 
        end = n - 1
        
        ans = score = 0 
        
        while start <= end: 
            if power >= tokens[start]:
                score += 1 
                
                power -= tokens[start]                
                start += 1 
                                
            elif ans > 0: 
                score -= 1 
                
                power += tokens[end]                
                end -= 1 
                
            else: 
                break
                
            ans = max(ans, score)
            
        return ans 
        
            
