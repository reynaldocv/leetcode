# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:        
        @cache 
        def helper(i, h, l, w): 
            if i == n: 
                return 0 
            
            hi, li, wi = cuboids[i]
            
            if hi <= h and li <= l and wi <= w: 
                return max(hi + helper(i + 1, hi, li, wi), helper(i + 1, h, l, w))
            else:
                return helper(i + 1, h, l, w)
        
        n = len(cuboids)
        
        for i in range(n):
            cuboids[i].sort(reverse = True)
        
        cuboids.sort(reverse = True)
        
        return helper(0, inf, inf, inf)

class Solution2:
    def maxHeight(self, cuboids: List[List[int]]) -> int:        
        dp = []
        for cuboid in cuboids:
            cuboid.sort()
        
        n = len(cuboids)
        cuboids.sort()
        
        dp = [0]*n
        
        test = lambda x,y: x[0] <= y[0] and x[1] <= y[1] and x[2] <= y[2]
        
        dp[0] = cuboids[0][2]
        
        for i in range(1,len(cuboids)):
            temp = 0
            for j in range(i):
                if test(cuboids[j], cuboids[i]):
                    temp = max(temp, dp[j])
                    
            dp[i] = temp + cuboids[i][2]
        
        return max(dp)
  
