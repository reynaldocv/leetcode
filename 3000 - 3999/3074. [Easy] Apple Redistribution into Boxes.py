# https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        
        heap = []
        
        for num in capacity: 
            heappush(heap, -num)
            
        ans = 0
            
        while heap and total > 0: 
            total += heappop(heap)
            
            ans += 1 
            
        return ans 
        
