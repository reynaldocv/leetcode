# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def helper(target):            
            start = -1
            
            end = n 
            
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
        
class Solution2:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        
        ans = 0 
        
        for num in arr1: 
            left = bisect_left(arr2, num - d)
            right = bisect_right(arr2, num + d)
            
            if left == right: 
                ans += 1 
                
        return ans 
        
class Solution3:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        
        ans = 0 
        
        for num in arr1: 
            left = bisect_left(arr2, num - d)
            right = bisect_left(arr2, num + d + 1)
            
            if left == right: 
                ans += 1 
                
        return ans 
        
