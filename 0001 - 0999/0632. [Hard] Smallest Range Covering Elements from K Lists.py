# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        k = len(nums)
        
        maxElem = 0 
        for i in range(k): 
            maxElem = max(maxElem, nums[i][0]) 
            heappush(heap, (nums[i][0], 0, i))
        
        ans = (maxElem - min(heap)[0], min(heap)[0])
        
        while heap: 
            (start, idx, i) = heappop(heap)
        
            idx += 1
            if idx == len(nums[i]):
                break
                
            else: 
                heappush(heap, (nums[i][idx], idx, i))
             
                maxElem = max(maxElem, nums[i][idx])
                ans = min(ans, (maxElem - heap[0][0], heap[0][0]))
                
        return [ans[1], ans[1] + ans[0]]
            
        
        
