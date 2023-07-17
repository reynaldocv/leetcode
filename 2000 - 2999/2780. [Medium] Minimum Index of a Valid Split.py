# https://leetcode.com/problems/minimum-index-of-a-valid-split/

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        maxElem = (-inf, inf)
        
        for num in nums: 
            counter[num] += 1 
            
            maxElem = max(maxElem, (counter[num], num))
        
        (rightCnt, dominant) = maxElem
        
        leftCnt = 0 
        
        n = len(nums)
        
        for (i, num) in enumerate(nums[: -1]):
            left = i + 1
            right = n - i - 1
            
            if num == dominant: 
                leftCnt += 1 
                rightCnt -= 1 
                
            if 2*leftCnt > left and 2*rightCnt > right: 
                return i 
        
        return -1
            
