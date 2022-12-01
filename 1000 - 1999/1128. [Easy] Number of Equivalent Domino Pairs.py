# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(lambda: 0)
        
        for (a, b) in dominoes:
            if a > b: 
                a, b = b, a
            
            counter[(a, b)] += 1 
            
        ans = 0 
        
        for key in counter: 
            ans += counter[key]*(counter[key] - 1)//2
                
        return ans 
        
