# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:        
        maxElem = 0
        
        ans = []
        
        tmp = 0
        
        for num in nums:
            maxElem = max(maxElem, num)
            
            tmp += num + maxElem
            
            ans.append(tmp)
            
        return ans
