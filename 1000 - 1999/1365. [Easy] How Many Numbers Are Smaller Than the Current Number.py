# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [num for num in nums]
        
        arr.sort() 
        
        ans = []
        
        for num in nums: 
            idx = bisect_left(arr, num)
            
            ans.append(idx)
            
        return ans 
        
