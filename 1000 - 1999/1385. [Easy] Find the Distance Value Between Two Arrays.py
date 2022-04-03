# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def helper(target):
            if target < arr2[0]:
                return 0 
            
            if arr2[-1] < target: 
                return n 
            
            start = -1
            end = n - 1
            
            while end - start > 1: 
                mid = (end + start)//2
                if arr2[mid] < target: 
                    start = mid
                else: 
                    end = mid
                    
            return end
                    
        n = len(arr2)
        
        arr2.sort()
        
        ans = 0 
        
        for num in arr1:         
            if helper(num + d + 1) == helper(num - d):                
                ans += 1 
            
        return ans 
        
