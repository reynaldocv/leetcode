# https://leetcode.com/problems/make-k-subarray-sums-equal/

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        step = gcd(n, k)
        
        ans = 0
        
        for i in range(step):
            nums = arr[i:: step]            
            nums.sort()
            
            median = nums[len(nums)//2]
            
            for num in nums:
                ans += abs(num - median)
                
        return ans
