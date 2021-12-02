# https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:     
        n = len(nums)
        ans = []
        
        m = 2*k + 1
        
        if n < m: 
            return [-1 for _ in range(n)]
        
        ans += [-1]*k
        
        aSum = sum(nums[:m])        
        ans.append(aSum//(m))
        
        for (i, num) in enumerate(nums[m: ]):            
            aSum += num - nums[i]
            ans.append(aSum//m)
            
        ans+= [-1]*k
        
        return ans
