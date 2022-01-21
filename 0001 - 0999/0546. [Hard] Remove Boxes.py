# https://leetcode.com/problems/remove-boxes/

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def helper(i, j, k):
            if i > j: 
                return 0
            
            cnt = 0
            while (i + cnt) <= j and boxes[i] == boxes[i + cnt]:
                cnt += 1
                
            i2 = i + cnt
            
            ans = helper(i2, j, 0) + (k + cnt)**2
            
            for m in range(i2, j + 1):
                if boxes[m] == boxes[i]:
                    ans = max(ans, helper(i2, m - 1, 0) + helper(m, j, k + cnt))
            
            return ans
        
        return helper(0, len(boxes) - 1, 0)
