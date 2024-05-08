# https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def helper(arr):
            left = []
            right = [num for num in arr]
        
            right.sort() 
        
            ans = 0 
            
            for (ith, num) in enumerate(arr):             
                start = bisect_left(left, num)
                end = len(right) - bisect_left(right, num + 1)
            
                ans += start*end
            
                idx = bisect_left(right, num)            
                right.pop(idx)
            
                insort(left, num)
            
            return ans 
        
        return helper(rating) + helper(rating[:: -1])
        
        
        
