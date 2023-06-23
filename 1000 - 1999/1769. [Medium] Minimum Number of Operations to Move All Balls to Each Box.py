# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        rightCnt = 0 
        rightSum = 0 
        
        for (i, num) in enumerate(boxes):
            if num == "1":
                rightCnt += 1 
                rightSum += i 
                
        leftCnt = 0 
        leftSum = 0 
        
        ans = []
        
        for (i, num) in enumerate(boxes):
            left = leftCnt*i - leftSum
            
            if num == "1":
                leftCnt += 1 
                leftSum += i 
                
            right = (rightSum - leftSum) - (rightCnt - leftCnt)*i
            
            ans.append(left + right)
            
        return ans 
