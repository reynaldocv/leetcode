https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def helper(value):
            ans = 0 
            prev = -inf
            for x in position: 
                if x - prev >= value:
                    ans += 1                     
                    prev = x
                    
            return ans
        
        position.sort()
        start = 1 
        end = position[-1] - position[0] + 1
        
        while end - start > 1: 
            mid = (end + start)//2
            if helper(mid) < m: 
                end = mid
            else:
                start = mid
                
        return start
