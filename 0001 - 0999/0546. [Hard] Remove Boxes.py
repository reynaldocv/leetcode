# https://leetcode.com/problems/remove-boxes/

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def helper(start, end, k):
            if start > end: 
                return 0
            
            cnt = 0
            while (start + cnt) <= end and boxes[start] == boxes[start + cnt]:
                cnt += 1
                
            newStart = start + cnt
            
            ans = helper(newStart, end, 0) + (k + cnt)**2
            
            for mid in range(newStart, end + 1):
                if boxes[mid] == boxes[start]:
                    ans = max(ans, helper(newStart, mid - 1, 0) + helper(mid, end, k + cnt))
            
            return ans
        
        n = len(boxes)
                
        return helper(0, n - 1, 0)
