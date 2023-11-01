# https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in nums:
            lvl = 0 
            
            while num: 
                bit = num % 2 
                
                if bit == 1: 
                    counter[lvl] += 1 
                    
                num //= 2 
                lvl += 1 
                
        ans = 0 
        
        for key in counter: 
            if counter[key] >= k: 
                ans += 2**key
                
        return ans 
            
        
        
        
