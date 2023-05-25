# https://leetcode.com/problems/total-cost-to-hire-k-workers/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        left = []
        right = []
        
        ans = 0 
        
        if 2*candidates > n: 
            for cost in costs: 
                heappush(left, cost)
                
            for _ in range(k):
                ans += heappop(left) 
                
        else: 
            start = 0 
            end = n - 1
            
            for _ in range(candidates):
                heappush(left, costs[start])
                start += 1 
                
                heappush(right, costs[end])
                end -= 1 
            
            for _ in range(k):
                val1 = left[0] if left else inf 
                val2 = right[0] if right else inf
                
                if val1 <= val2: 
                    ans += heappop(left)
                    
                    if start <= end: 
                        heappush(left, costs[start])
                    
                        start += 1 
                    
                else: 
                    ans += heappop(right)
                    
                    if start <= end: 
                        heappush(right, costs[end])
                    
                        end -= 1 
                        
        return ans 
