# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        nums.sort()
        
        arr = []
        for i in range(n - 1):
            arr.append(nums[i + 1] - nums[i])
        
        ans = 1
        aSum = aSum2 = 0
        lenght = 1
        i = 0 
        for num in arr: 
            aSum += num
            aSum2 += num * lenght        
            if aSum2 <= k: 
                ans = max(ans, lenght + 1)    
                
            else:                
                while aSum2 > k: 
                    aSum2 -= aSum
                    aSum -= arr[i]                    
                    lenght -= 1
                    i += 1                    
                    
            lenght += 1
            
        return ans
