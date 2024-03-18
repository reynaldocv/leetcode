# https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        seen = set() 
        
        aSum = sum(nums)
        
        heap = []
        
        for (i, num) in enumerate(nums):
            heappush(heap, (num, i))
            
        ans = []
            
        for (ith, k) in queries: 
            if ith not in seen: 
                seen.add(ith)
                
                aSum -= nums[ith]
                
            for _ in range(k): 
                while heap and heap[0][1] in seen: 
                    heappop(heap)
                    
                if heap: 
                    (elem, ith)  = heappop(heap)
                    
                    aSum -= elem
                    seen.add(ith)
                    
                else: 
                    break 
                
            ans.append(aSum)
            
        return ans 
        
