https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        if k >= n: 
            return sum(cardPoints)
        
        leftSum = list(cardPoints)
        rightSum = list(cardPoints)
        
        for i in range(1, k + 1):
            leftSum[i] += leftSum[i - 1]
            rightSum[n - i - 1] += rightSum[n - i]
            
        ans = 0 
        for i in range(-1, k):
            left = leftSum[i] if i != -1 else 0 
            right = rightSum[n - k + i + 1] if n - k + i + 1 != n else 0
            
            ans = max(ans, left + right)
            
        return ans
        
