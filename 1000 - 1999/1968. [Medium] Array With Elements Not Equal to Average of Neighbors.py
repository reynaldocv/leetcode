https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        nums.sort()
        
        start = 0 
        middle = n//2
        
        if n % 2 == 1: 
            middle += 1
            
        ans = []
        
        turn = 1 
        
        for _ in range(n): 
            if turn == 1: 
                ans.append(nums[start])
                
                start += 1 
                
            else:
                ans.append(nums[middle])
                
                middle += 1 
                
            turn = 1 - turn 
            
        return ans 
            
        
        
            
