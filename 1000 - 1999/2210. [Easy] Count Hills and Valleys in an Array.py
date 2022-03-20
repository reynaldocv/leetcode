# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev = -inf
        arr = []
        for num in nums: 
            if num != prev: 
                arr.append(num)
            
            prev = num
        
        n = len(arr)
        ans = 0 
        
        for i in range(1, n - 1):
            if arr[i - 1] > arr[i] and arr[i + 1] > arr[i]:
                ans += 1 
                
            if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                ans += 1 
                
        return ans
