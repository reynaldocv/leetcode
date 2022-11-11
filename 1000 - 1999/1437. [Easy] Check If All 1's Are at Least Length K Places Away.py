# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cnt = k 
        
        for num in nums: 
            if num == 0: 
                cnt += 1 
            else:     
                if cnt < k: 
                    return False
                cnt = 0 
                
        return True 

                
        
