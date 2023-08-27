# https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache 
        def helper(start, k):
            if start == last: 
                return True 
            
            else: 
                for middle in range(start + k - 1, start + k + 2):
                    if middle in seen and middle > start: 
                        if helper(middle, middle - start):
                            return True 
                        
                return False 
            
        seen = {stone for stone in stones}
        
        begin = stones[0]
        last = stones[-1]
        
        return helper(begin, 0)
        
        
