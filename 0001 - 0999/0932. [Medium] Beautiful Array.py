

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def helper(num):
            if num == 1:
                return [1]
            
            odds = helper((num + 1)//2)
            evens = helper(num//2)
            
            return [2*elem - 1 for elem in odds] + [2*elem for elem in evens]
        
        return helper(n)
        
        
