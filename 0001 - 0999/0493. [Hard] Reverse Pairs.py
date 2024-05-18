# https://leetcode.com/problems/reverse-pairs/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = []        
        ans = 0 
        
        for num in nums[:: -1]:
            idx = bisect_left(arr, (num + 1)//2)
            
            ans += idx
            
            insort(arr, num)
            
        return ans 
            
            
        
