# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr) 
        
        left = [arr[0]]
            
        for num in arr[1: ]:
            if left[-1] <= num: 
                left.append(num)

            else: 
                break 
                
        l = len(left)
                
        if n == l:
            return 0 
        
        right = [arr[-1]]
        
        for num in arr[: n - 1][:: -1]:
            if num <= right[0]: 
                right.insert(0, num)

            else: 
                break 

        r = len(right)
                
        ans = n - max(l, r)
        
        for (i, num) in enumerate(left): 
            idx = bisect_left(right, num)
            
            ans = min(ans, n - (i + r - idx + 1))
            
        return ans 
            
