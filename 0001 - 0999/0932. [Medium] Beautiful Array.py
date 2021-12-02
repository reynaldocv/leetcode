

class Solution:
    def beautifulArray(self, n: int) -> List[int]:  
        @cache
        def helper(num):
            if num == 1: 
                return [1]
            
            odds = helper((num + 1)//2)
            evens = helper(num//2)
            ans = [2*x - 1 for x in odds] + [2*x for x in evens]
            
            return ans
            
        
        return helper(n)
     
        
