# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0 
        arr = []
        idx = {}
        start = -1
        for (i, fruit) in enumerate(fruits): 
            idx[fruit] = (i, fruit)
            if len(idx) == 3: 
                minIdx = min([idx[key] for key in idx])
                start = minIdx[0]
                idx.pop(minIdx[1])
            
            ans = max(ans, i - start)
            
        return ans
            
                
                
            
                
            
