# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = 0 
        left = [0 for i in range(n)]
        for (i, num) in enumerate(nums): 
            if num == 0: 
                cnt += 1 
            left[i] = cnt
        
        right = [0 for i in range(n)]
        cnt = 0 
        for (i, num) in enumerate(nums[::-1]): 
            if num == 1: 
                cnt += 1 
            right[~i] = cnt
        
        arr = []
        maxElem = 0
        for i in range(n + 1):
            l = left[i - 1] if i > 0 else 0
            r = right[i] if i < n else 0 
            arr.append((l + r, i))
            maxElem = max(maxElem, l + r)
        
        ans = [i for (s, i) in arr if s == maxElem]
        
        return ans
        
    
        
        
