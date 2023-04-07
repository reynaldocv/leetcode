# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def helper(a, b):
            if a % b == 0: 
                return b 
            
            return helper(b, a % b)
        
        counter = defaultdict(lambda: 0)
        
        for num in deck: 
            counter[num] += 1 
            
        ans = counter[deck[0]]
        
        for key in counter: 
            ans = helper(ans, counter[key])
            
        return ans >= 2
        
        
        
        
