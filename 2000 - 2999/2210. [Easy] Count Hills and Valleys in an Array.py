# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums) 
        
        prev = -inf         
        
        arr = []
        
        for num in nums:
            if prev != num:
                arr.append(num)
                
            prev = num 
                
        ans = 0 
        
        m = len(arr)
        
        for i in range(1, m - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                ans += 1 
                
            elif arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
                ans += 1 
                
        return ans 
