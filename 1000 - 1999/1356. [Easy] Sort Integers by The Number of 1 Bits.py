# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def helper(num):
            ans = 0 
            
            while num: 
                if num % 2 == 1: 
                    ans += 1 
                    
                num //= 2 
                
            return ans 
        
        arr.sort(key = lambda item: (helper(item), item))
        
        return arr
        
