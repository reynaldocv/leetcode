# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = [num for num in nums if num < 0]
        positives = [num for num in nums if num >= 0]
        
        n = len(negatives)
        ans = []
        
        for i in range(n):
            ans.append(positives[i])
            ans.append(negatives[i])
            
        return ans
        
        
