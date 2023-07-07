# https://leetcode.com/problems/intervals-between-identical-elements/

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        rightSum = defaultdict(lambda: 0)
        rightCnt = defaultdict(lambda: 0)
        
        for (i, num) in enumerate(arr):
            rightSum[num] += i 
            rightCnt[num] += 1 
            
        leftSum = defaultdict(lambda: 0)
        leftCnt = defaultdict(lambda: 0)
        
        ans = []
        
        for (i, num) in enumerate(arr):
            rightCnt[num] -= 1 
            rightSum[num] -= i 
            
            ans.append(i*leftCnt[num] - leftSum[num] + rightSum[num] - i*rightCnt[num])
            
            leftCnt[num] += 1 
            leftSum[num] += i 
            
        return ans 
