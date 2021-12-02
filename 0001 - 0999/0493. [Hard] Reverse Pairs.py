# https://leetcode.com/problems/reverse-pairs/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = []
        ans = 0 
        for num in nums: 
            idx = bisect_right(arr, num*2)
            ans += len(arr) - idx            
            insort_left(arr, num)
        
        return ans
        
