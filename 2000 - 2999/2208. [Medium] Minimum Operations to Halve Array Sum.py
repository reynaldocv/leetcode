# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        aSum = 0 
        for num in nums: 
            heappush(heap, -num)
            aSum += num 
            
        ans = 0 
        aux = 0 
        while aux < aSum/2:
            elem = heappop(heap)
            aux -= elem/2
            heappush(heap, elem/2)
            
            ans += 1 
            
        return ans 
