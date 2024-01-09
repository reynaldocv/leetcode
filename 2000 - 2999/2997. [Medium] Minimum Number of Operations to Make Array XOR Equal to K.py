class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0 
        tmp = 0 
        
        for num in nums: 
            tmp ^= num 
            
        while k > 0 or tmp > 0: 
            if k & 1 != tmp & 1: 
                ans += 1 

            tmp //= 2 
            k //= 2
                
        return ans 
                    
                    
