# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []        
        for num in nums: 
            if len(arr) == 0 or arr[-1] < num: 
                arr.append(num)
            else: 
                idx = bisect_left(arr, num)
                arr[idx] = num
             
        return len(arr)
        
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1]*n
        ans = 1
        for i in range(1, n):
            maxElem = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxElem = max(maxElem, arr[j])                    
            arr[i] = maxElem + 1
            ans = max(ans, arr[i])
        
        return ans
    

        
        
