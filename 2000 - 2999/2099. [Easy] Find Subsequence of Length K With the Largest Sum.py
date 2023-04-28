# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        
        for (i, num) in enumerate(nums):
            heappush(heap, (-num, i))
            
        arr = []
        
        for _ in range(k):
            (num, i) = heappop(heap)
            
            arr.append((i, -num))
            
        arr.sort() 
        
        ans = []
        
        for (_, num) in arr: 
            ans.append(num)
            
        return ans 
            
        
        
        
  
                
                
        
            
        
