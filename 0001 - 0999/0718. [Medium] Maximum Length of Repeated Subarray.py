# https://leetcode.com/problems/maximum-length-of-repeated-subarray/


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:        
        m, n = len(nums1), len(nums2)
            
        index = defaultdict(lambda: [])
        for (i, num) in enumerate(nums1):
            index[num].append(i)
        
        dp = [[0 for i in range(n + 1)] for _ in range(m + 1)]
    
        ans = 0 
        
        for (j, num) in enumerate(nums2):
            for i in index[num]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            
                ans = max(ans, dp[i + 1][j + 1])
                
        return ans 
    
class Solution2:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        ans = 0 
        
        for i in range(1, m + 1):
            for j in range(1, n  + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else: 
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
                    
        return ans
        
        
