# https://leetcode.com/problems/video-stitching/

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [inf for _ in range(time + 1)]
        dp[0] = 0
        
        for i in range(1, time + 1):
            for (start, end) in clips:
                if start <= i <= end:
                    dp[i] = min(dp[start] + 1, dp[i])
                    
        return dp[time] if dp[time] != inf else -1 
        
        
